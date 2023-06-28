# API接口文档模板

本文档更新时间：2022-12-07

本文档更新说明：提供了接口文档模板，后续如果有接口文档编写相关工作，可以参考该模板。



**接口名称：** 微博帐号基础信息批量获取接口  <font color="red">【接口名称，见名知意】</font>

**接口版本：** v1.0.0 <font color="red">【接口版本号】</font>

**接口地址：** `http://dist.sina.com/api/account/get_list_sina` <font color="red">【接口地址需要拼接URL+端口号，默认端口号80】</font>

**请求方式：** GET/POST <font color="red">【接口的请求方式，GET或POST】</font>

**请求头（Header）参数：**

| 字段名      | 类型   | 描述                                  |
| ----------- | ------ | ------------------------------------- |
| app-key     | string | 合作商身份标识                        |
| api-version | string | 请求接口版本号                        |
| timestamp   | string | 接口请求访问时间，2022-12-07 19:08:30 |

<font color="red">【注：接口若有请求头（Header）参数，需要填写参数的字段名称、字段类型、该字段的必要文字描述。也可以新添加一列，描述字段的默认值。】</font>

**请求体（Body）参数：**

| 字段名       | 类型   | 描述                                                         |
| ------------ | ------ | ------------------------------------------------------------ |
| page         | int    | 页码，默认值为1                                              |
| perpage      | int    | 每页返回微博账号的数量，默认100                              |
| sort         | string | 排序字段，默认为1正序，2倒序。支持最多5个字段排序，多个排序字段用","隔开，例如：price_post-1, klr_index-2 |
| account_uid  | string | 微博账号uid                                                  |
| media_id     | string | 账号唯一标识id                                               |
| follower_max | int    | 粉丝数上限                                                   |
| follower_min | int    | 粉丝数下限                                                   |

<font color="red">【注：请求体（Body）参数中，需要填写参数的字段名称、字段类型、该字段的必要文字描述。】</font>

**返回参数：**

| 字段名            | 类型   | 描述                   |
| ----------------- | ------ | ---------------------- |
| account_uid       | string | 微博账号UID            |
| account_name      | string | 微博账号昵称           |
| account_class     | string | 帐号分类               |
| account_followers | string | 帐号粉丝量             |
| media_id          | int    | 资源中心账号唯一标识ID |
| avatar            | string | 微博头像的URL链接      |
| account_desc      | string | 微博账号描述           |
| verified_reason   | string | 微博大V认证描述        |
| klr_index         | int    | 克劳锐指数             |
| article_count     | int    | 微博账号博文数量       |

<font color="red">【注：需要介绍接口返回参数中的核心字段，如：字段名、字段类型、字段描述。】</font>

**返回示例：**

```json
{
    "code": 10000,
    "msg": "请求成功",
    "data": {
        "pagination": {
            "has_next": false,
            "current_page": 1,
            "total_page": 1,
            "total_count": 1,
            "perpage": 100
        },
        "data": [
            {
                "account_uid": "1344360230",
                "account_name": "Kevin凯文老师",
                "account_class": [
                    "美妆时尚"
                ],
                "account_followers": 54863320,
                "avatar": "http://tvax4.sinaimg.cn/crop.90.414.792.792.180/50214f26ly8g1oaw8s0rrj20u01900x1.jpg",
                "account_desc": "会摄影会做饭、喜欢血拼种草的“彩妆小弟”，当然你如果想跟我学英语也是可以的…",
                "verified_reason": "著名造型师 微博故事红人 微博签约自媒体",
                "article_count": 14530,
                "klr_index": "89.4",
                "media_id": 740131,
            }
        ]
    }
}
```

<font color="red">【注：在返回示例的位置粘贴返回的json代码，方便看清接口返回的层次信息。】</font>

**异常返回示例：**

```json
{
    "code": 10002,
    "msg": "签名错误",
    "data": []
}
```

<font color="red">【注：需要介绍非成功状态下的接口返回示例，方便接口调用方做异常处理。】</font>

**常见的接口状态返回码：**

| 字段  | 描述           |
| :---- | :------------- |
| 10000 | 请求成功       |
| 10001 | 客户端身份异常 |
| 10002 | 签名错误       |
| 10003 | 访问次数频繁   |
| 10004 | 接口参数异常   |
| 10005 | 接口限制访问   |

