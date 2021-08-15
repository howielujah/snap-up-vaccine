import cv2
import numpy as np
# import datetime
import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance


class snap(object):
    chromedriver = '你本機的 chromedriver 位置'

    def __init__(self):
        # print(datetime.datetime.now())
        self.driver = webdriver.Chrome(snap.chromedriver)
        # 設定最大等待時間，避免阻塞
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        # 網頁url
        self.url = 'https://rmsvc.sph.org.tw/Residue.aspx'
        self.driver.maximize_window()

    def __get_screenshot(self):
        self.driver.save_screenshot('web.png')
        location = self.driver.find_element_by_id('imgCode').location
        size = self.driver.find_element_by_id('imgCode').size
        left = 2 * location['x']
        top = 2 * location['y']
        right = left + 2 * size['width']
        bottom = top + 2 * size['height']
        imgcode = Image.open('web.png').crop(
            (left, top, right, bottom))
        imgcode = imgcode.convert('L')  # 轉換模式：L | RGB
        imgcode = ImageEnhance.Contrast(imgcode)  # 增強對比度
        imgcode = imgcode.enhance(2.0)  # 增加飽和度
        file_name = 'authcode.png'
        imgcode.save(file_name)
        return file_name

    def __analyze_code(self, file_name):
        _, thresh = cv2.threshold(cv2.imread(
            file_name, 0), 0, 255, cv2.THRESH_BINARY)
        thresh = cv2.filter2D(
            thresh, -1, 1/16 * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]))
        cv2.imwrite('thresh.png', thresh)
        return pytesseract.image_to_string('thresh.png')

    def run(self):
        try:
            # print(datetime.datetime.now())
            self.driver.get(self.url)
            # self.driver.switch_to.alert.accept()
            # 填入個人資料
            self.driver.find_element_by_id('pname').send_keys('你的名字')
            self.driver.find_element_by_id('idno').send_keys('你的身分證字號')
            self.driver.find_element_by_id('rmsdata').send_keys('你的西元出生年月日')
            self.driver.find_element_by_id('lineid').send_keys('你的聯絡電話')
            self.driver.find_element_by_id('cellphone').send_keys('你的手機號碼')
            # 截圖驗證碼
            file_name = self.__get_screenshot()
            code = self.__analyze_code(file_name)
            self.driver.find_element_by_id('txt_input').send_keys(code.strip())
            self.driver.find_element_by_id('applybtn').click()
            print(code.strip())
            # self.driver.quit()
        except Exception as e:
            print(str(e))
            # print("載入頁面太慢，停止載入")
            self.driver.execute_script(
                "window.stop()")    # 這裡是防止網頁一直載入不能之後後面程式碼


if __name__ == '__main__':
    auto_snap = snap()
    auto_snap.run()
