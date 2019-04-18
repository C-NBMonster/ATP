
var resultData = {
"testPass": 0,
"testResult": [
    {
        "className": "_FailedTest",
        "methodName": "test_sh_300079_4_0",
        "description": null,
        "spendTime": "0.0 s",
        "status": "失败",
        "log": [
            "",
            "Traceback (most recent call last):\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\case.py\", line 59, in testPartExecutor\n    yield\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\case.py\", line 605, in run\n    testMethod()\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 34, in testFailure\n    raise self._exception\n",
            "ImportError: Failed to import test module: test_sh_300079_4_0\nTraceback (most recent call last):\n  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 428, in _find_test_path\n    module = self._get_module_from_name(name)\n  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 369, in _get_module_from_name\n    __import__(name)\n  File \"D:\\Py_Projects\\django_projects\\jytest-u-0104\\livecase\\test_sh_300079_4_0.py\", line 26\n    pc_ip = \"127.0.0.1\" #默认勿删\n        ^\nIndentationError: expected an indented block\n\n"
        ]
    },
    {
        "className": "_FailedTest",
        "methodName": "test_sh_300079_8_0",
        "description": null,
        "spendTime": "0.001 s",
        "status": "失败",
        "log": [
            "",
            "Traceback (most recent call last):\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\case.py\", line 59, in testPartExecutor\n    yield\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\case.py\", line 605, in run\n    testMethod()\n",
            "  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 34, in testFailure\n    raise self._exception\n",
            "ImportError: Failed to import test module: test_sh_300079_8_0\nTraceback (most recent call last):\n  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 428, in _find_test_path\n    module = self._get_module_from_name(name)\n  File \"D:\\Python\\Python36\\lib\\unittest\\loader.py\", line 369, in _get_module_from_name\n    __import__(name)\n  File \"D:\\Py_Projects\\django_projects\\jytest-u-0104\\livecase\\test_sh_300079_8_0.py\", line 26\n    pc_type = \"android真机：魅族not6\" #默认勿删\n          ^\nIndentationError: expected an indented block\n\n"
        ]
    }
],
"testName": "即有生活用例执行情况：",
"testAll": 2,
"testFail": 2,
"beginTime": "2019-02-14 11:46:13",
"totalTime": "0s",
"testSkip": 0,
"testError": 0
};
function details(obj) {
    if ($(obj).text() == '展开') {
        var len = $(obj).parent().parent().children().length;
        var detailLog = "";
        var logs = resultData["testResult"][parseInt($(obj).attr("buttonIndex"))]["log"];
        $(obj).text("收缩");
        $(obj).removeClass("btn-primary");
        $(obj).addClass("btn-danger");
        $.each(logs, function (i, n) {
            detailLog = detailLog + "<p>" + n + "</p>";
        });
        $(obj).parent().parent().after("<tr><td colspan='" + len + "'><div style='font-family: Consolas;font-size:12px'>" + detailLog + "</div></td></tr>");
    } else if ($(obj).text() == '收缩') {
        $(obj).parent().parent().next().remove();
        $(obj).text("展开");
        $(obj).removeClass("btn-danger");
        $(obj).addClass("btn-primary");
    }

}
$(function () {
    $("#testName").text(resultData["testName"]);
    $("#testPass").text(resultData["testPass"]);
    $("#testFail").text(resultData["testFail"]);
    $("#testSkip").text(resultData["testSkip"]);
    $("#testAll").text(resultData["testAll"]);
    $("#beginTime").text(resultData["beginTime"]);
    $("#totalTime").text(resultData["totalTime"]);
    var classNames = [];
    var results = [];
    $.each(resultData["testResult"], function (i, n) {
        if(classNames.indexOf(n["className"])==-1){
            classNames.push(n["className"]);
        }
        if(results.indexOf(n["status"])==-1){
            results.push(n["status"]);
        }
    });

    $.each(classNames, function (i, n) {
        $("#filterClass").append("<option value='"+n+"' hassubinfo='true'>"+n+"</option>");
    });
    $.each(results, function (i, n) {
        $("#filterResult").append("<option value='"+n+"' hassubinfo='true'>"+n+"</option>");
    });

    $("#filterClass").chosen({search_contains: true});
    $("#filterResult").chosen({search_contains: true});

    function generateResult(className, caseResult) {
        $("#detailBody").children().remove();
        var filterAll = 0;
        var filterOk = 0;
        var filterFail = 0;
        var filterSkip = 0;
        $.each(resultData["testResult"], function (i, n) {
            if((className=="" || n["className"]==className) && (caseResult=="" || n["status"]==caseResult)){
                filterAll += 1;
                var status = "";
                if (n["status"] == '成功') {
                    filterOk += 1;
                    status = "<td><span class='text-navy'>成功</span></td>";
                } else if (n["status"] == '失败') {
                    filterFail += 1;
                    status = "<td><span class='text-danger'>失败</span></td>";
                } else if (n["status"] == '跳过') {
                    filterSkip += 1;
                    status = "<td><span class='text-warning'>跳过</span></td>";
                } else {
                    status = "<td><span>" + n["status"] + "</span></td>";
                }
                var tr = "<tr style='font-family: Consolas'>" +
                    "<td>" + (i + 1) + "</td>" +
                    "<td>" + n["className"] + "</td>" +
                    "<td>" + n["methodName"] + "</td>" +
                    "<td>"+n["description"] + "</td>" +
                    "<td>" + n["spendTime"] + "</td>" +
                    status + "<td><button type='button' onclick='details(this)' buttonIndex='" + i + "' class='btn btn-primary btn-xs' style='margin-bottom: 0px'>展开</button></td></tr>"
                $("#detailBody").append(tr);
            }
        });
        $("#filterAll").text(filterAll);
        $("#filterOk").text(filterOk);
        $("#filterFail").text(filterFail);
        $("#filterSkip").text(filterSkip);
    }

    generateResult("", "");

    $("#filterClass").on('change', function () {
        var className = $("#filterClass").val();
        var caseResult = $("#filterResult").val();
        generateResult(className, caseResult);
    });

    $("#filterResult").on('change', function () {
        var className = $("#filterClass").val();
        var caseResult = $("#filterResult").val();
        generateResult(className, caseResult);
    });

    //$(".chosen-select").trigger("chosen:updated");

    function pie() {
        var option = {
            title: {
                text: '测试用例运行结果',
                subtext: '',
                x: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: ['失败', '跳过', '成功']
            },
            series: [
                {
                    name: '运行结果',
                    type: 'pie',
                    radius: '55%',
                    center: ['50%', '60%'],
                    data: [
                        {value: resultData["testFail"], name: '失败'},
                        {value: resultData["testSkip"], name: '跳过'},
                        {value: resultData["testPass"], name: '成功'}
                    ],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };
        var chart = echarts.init(document.getElementById("echarts-map-chart"));
        chart.setOption(option);
    }
    pie();
});
