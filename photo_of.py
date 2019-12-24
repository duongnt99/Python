from crawler.images.common_image import CommonImage
from crawler.init.constants import IMAGE
import sys

class PhotoOf(CommonImage):
    def execute_script(self, link_user: str):
        self.driver.get(self.get_link_photos_of(link_user))
        self.scroll()
        elements = self.safe_get_elements_by_xpath(IMAGE['XPATH_EACH_IMAGE'])
        images = self.get_link_images(elements)
        link_images = self.get_download_images_url(images)
        link_images = [(link, [box for box in boxs if box != ''])  for link, boxs in link_images if link != "None"]
        print(link_images)
        # nay mai se chuyen link download cho queue download
        # self.image_downloader(link_images, self.create_original_link(link_user))

    def get_link_photos_of(self, link_user: str) -> str:
        original_link = self.create_original_link(link_user)
        link_photo_all = original_link + "/photos_of"
        return link_photo_all.replace("//", "/")