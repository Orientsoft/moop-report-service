# moop-report-service
moop report service
### api
reportInRequest
```js
{
    'operation':'preview', //download
    'title':'专题名称<PYTHON>',
    'teacher_name':'老师名称',
    'teacher_prof':'老师职称',
    'total':'12',
    'project_count':'12',
    'study_time':'30小时',
    'desc':'python系列教学课程，包含python基础及python进阶',
    'img1':'http://moop-dev.oss-cn-shenzhen.aliyuncs.com/bar.png',
    'img2':'http://moop-dev.oss-cn-shenzhen.aliyuncs.com/bar.png',
    'student':[
        {
            'realname':'user真实名字',
            'certification':'学号',
            'times':'10小时',
            'count':'4次',
            'score':'A+',
            'feedback':'教师评语',
            'img1':'http://moop-dev.oss-cn-shenzhen.aliyuncs.com/bar.png',
            'img2':'http://moop-dev.oss-cn-shenzhen.aliyuncs.com/bar.png',
        }
    ]
}
```
reportInResponse
```js
{
    'result':'字符串内容'
}
```
```python
resp = make_response(result)
if (operation == 'download'){
    resp.headers["Content-Disposition"] = (
        "attachment; filename='{0}'; filename*=UTF-8''{0}".format('报告.pdf'))
    resp.headers['Content-Type'] = 'application/pdf'
}
return resp
```
| method | path | query | request | response | remark |
| ------ | ---- | ----- | ------- | -------- | ------ |
| POST | /report | ----- | reportInRequest | reportInResponse | 状态码200为成功，其他为失败 |

