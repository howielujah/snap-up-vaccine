# 搶疫苗殘劑機器人
> 以此網址為測試目標 https://rmsvc.sph.org.tw/Residue.aspx

## 事前準備

### 下載並安裝 chromedriver 
下載網址: [chromedriver](http://chromedriver.chromium.org/)

1. Mac 需要把解壓縮後的安裝檔放入 `/usr/local/bin`  
2. 放進目錄後開啟 terminal 編輯檔案目錄的附加屬性  
```
cd /usr/local/bin
xattr -d com.apple.quarantine chromedriver
```
### 下載並安裝 tesseract
* Mac 可用 homebrew 安裝 `brew install tesseract`


### 安裝需要的套件 
1. `pip install -r requirements.txt`
3. 打開本地安裝 pytesseract 包中的 pytesseract.py 文件
4. 把 `tesseract_cmd = 'tesseract'` 後面的路徑改為自己本地 tesseract 執行文件的路徑。如我本機的文件路徑為：  
`tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'`

### 修改成自己的個資

### 執行
`python3 snap.py`