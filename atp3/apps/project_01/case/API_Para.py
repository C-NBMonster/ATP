# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: API_Para.py
@time: 2019/7/3 13:46
@desc: 
"""
# 发送POST请求的json数据

class API_Parameters():


    def skiplivingbody(self, userid):
        #插入图片，跳过活体
        postparams = {
            "saveTypeName": "livenessInfo",
            "saveContent": {
                "photoVOList": [
                    {
                        "fileName": "group1/M00/41/B9/CgoLiF0UZseAAEzGAACbyzv9ue4292.jpg",
                        "photoType": "52"
                    },
                    {
                        "fileName": "group1/M00/41/B9/CgoLiF0UZseAVFmcAACeORFhoYs604.jpg",
                        "photoType": "52"
                    },
                    {
                        "fileName": "group1/M00/41/B9/CgoLiF0UZseAcAQxAACfDGOg-xM043.jpg",
                        "photoType": "52"
                    },
                    {
                        "fileName": "group1/M00/41/B9/CgoLiF0UZseAPRBhAAChMMOxR4w858.jpg",
                        "photoType": "52"
                    }
                ],
                "fileName": "group2/M08/24/29/CgsMMFyxXj2AGqUTAABr8fiEcSk339.png",
                "photoType": "52",
                "biz_no": "30acb83c-53e1-4b72-94e5-1a3e951dfc71",
                "token_video": "c554ac43d9a08bff75e64232bf65c5d8",
                "request_id": "1547118731,d4f28ecc-6e30-4e86-aace-393eb4965e45",
                "passed": True,
                "liveness_score": 0,
                "image_timestamp": 0.840522
            },
            "userId": userid
        }

        return postparams

    def handDecisionCredit(self, idCredit):
        #手动执行决策
        hdc = [
            {
                "idCredit": idCredit,
                "status": "string"
            }
        ]

        return hdc


