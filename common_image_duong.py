import sys
import urllib.request
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from crawler.utilities.utilities import CommonUtilities
from crawler.init.constants import IMAGE


class CommonImage(CommonUtilities):
    def get_link_images(self, elements):
        try:
            return [x.get_attribute('href') for x in elements]
        except:
            print("Exception (Images)", sys.exc_info()[0])
        return None

    def parse_position_from_str(self, style):
        string = style.split(";")
        width = string[0].split(": ")[1]
        height = string[1].split(": ")[1]
        left = string[2].split(": ")[1]
        top = string[3].split(": ")[1]
        return width, height, left, top
    
    def parse_tagbox(self, tag):
        result = {}
        style = tag.get_attribute("style")     
        if style == '':
            return None
        id =  tag.get_attribute("id")

        width, height, left, top = self.parse_position_from_str(style)
        if id.find('tag') != -1:
            result['id'] = id.split(":")[-1]
        else:
            result['id'] = None
        result['width'] = width
        result['height'] = height
        result['left'] = left
        result['top'] = top

        return result

    def get_download_images_url(self, img_links):
        urls = []

        for link in img_links:
            if link != "None":
                valid_url_found = False
                self.driver.get(link)

                try:
                    while not valid_url_found:
                        WebDriverWait(self.driver, self.timeout_second).until(EC.presence_of_element_located((By.CLASS_NAME, "spotlight")))
                        element = self.driver.find_element_by_class_name("spotlight")
                        img_url = element.get_attribute('src')

                        if img_url.find('.gif') == -1:
                            valid_url_found = True
                            tag_elements = self.safe_get_elements_by_css_selector(IMAGE['CSS_TAGS_BOX'])
                            if tag_elements is not None:
                                if len(tag_elements) > 0:
                                    tag_box = [self.parse_tagbox(tag) for tag in tag_elements]
                                    tag_box = [tag for tag in tag_box if tag is not None]
                                    urls.append((img_url, tag_box))
                except Exception as e:
                    print(e)
            else:
                print(e)

        return urls

    def get_filename_from_link(self, link):
        return (link.split('.jpg')[0]).split('/')[-1] + '.jpg'

    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def download_from_url(self, link, filepath, img_name):
        print("Downloading ", img_name)
        try:
            urllib.request.urlretrieve(link, filepath)
            return img_name
        except:
            return None
        
    def image_downloader(self, img_links, original_link):
        folder_name = original_link.split("/")[-1]

        img_names = []

        try:
            try:
                folder = os.path.join(os.getcwd(),"data", folder_name)
                self.create_folder(folder)
            except Exception:
                print("Error in changing directory.")

            arr_download = [(link, self.get_filename_from_link(link), boxs) for link, boxs in img_links]
            arr_download = [(link, filename, boxs) for (link, filename, boxs) in arr_download if (filename != "10354686_10150004552801856_220367501106153455_n.jpg")]
            arr_download = [(link, os.path.join(folder, filename), filename, boxs) for link, filename, boxs in arr_download]

            img_names = [(link, filepath, self.download_from_url(link, filepath, filename), boxs) for (link, filepath, filename, boxs) in arr_download]
            print(img_names)
            img_names = [(link, filepath, filename, boxs) for (link, filepath, filename, boxs) in arr_download if filename is not None]
        except Exception as e:
            print("Exception (image_downloader):", e)

        return img_names