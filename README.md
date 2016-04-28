#Virusbook_Scanner
##程序功能
对目录中的样本实现批量上传，并获得检测报告，包括二十几种反病毒软件的检测结果。

Virusbook.cn可注册后申请自己的API，在`mypostfeile.py`、`vbquery.py`中修改相应的API字段值。

##程序结构
- `samples-malware`： 恶意样本目录，对应的文件清单保存在`samples-malware.txt`
- `samples-normal`： 正常样本目录，对应的文件清单保存在`samples-normal.txt`
- `mypostfeile.bat`： 上传样本到Virusbook的服务器
- `sha256_calc.py`： 批量获得文件的sha256值
- `myvbquery.bat`： 根据文件的sha256值，查询获得样本的扫描报告，并保存为csv格式
