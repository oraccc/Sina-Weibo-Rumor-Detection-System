function fnW(str) {
    var num;
    str >= 10 ? (num = str) : (num = "0" + str);
    return num;
}
//获取当前时间
var timer = setInterval(function () {
    var zh_day = ['日','一','二','三','四','五','六'];
    var date = new Date();
    var year = date.getFullYear(); //当前年份
    var month = date.getMonth(); //当前月份
    var data = date.getDate(); //天
    var hours = date.getHours(); //小时
    var minute = date.getMinutes(); //分
    var second = date.getSeconds(); //秒
    var day = zh_day[date.getDay()]; //获取当前星期几
    var ampm = hours < 12 ? "A.M." : "P.M.";
    $("#time").html(fnW(hours) + ":" + fnW(minute) + ":" + fnW(second));
    $("#date").html(
        "<span>" +
            year +
            "/" +
            (month + 1) +
            "/" +
            data +
            "</span><span>" +
            ampm +
            "</span><span>周" +
            day +
            "</span>"
    );
}, 1000);

$(".select").on("blur", function () {
    $(this).find(".select-ul").hide();
});
//下拉框点击出现下拉框内容
$(".select-div").on("click", function () {
    if ($(this).siblings(".select-ul").is(":hidden")) {
        $(this).siblings(".select-ul").show();
    } else {
        $(this).siblings(".select-ul").hide();
    }
});

$(".select-ul").on("click", "li", function () {
    $(this)
        .addClass("active")
        .siblings("li")
        .removeClass("active")
        .parent()
        .hide()
        .siblings(".select-div")
        .html($(this).html());
    var parentDiv = $(this).parent().parent().parent();
});

//鼠标滑动到按钮，按钮内容变成白色
var imgName;
$(".title-box")
    .children("button")
    .hover(
        function () {
            imgName = $(this).children("img").attr("src").split(".png")[0];
            $(this)
                .children("img")
                .attr("src", imgName + "_on.png");
        },
        function () {
            $(this)
                .children("img")
                .attr("src", imgName + ".png");
        }
    );

var startColor = [
    "#0e94eb",
    "#c440ef",
    "#efb013",
    "#2fda07",
    "#d8ef13",
    "#5f6fde",
    "#0eebc4",
    "#f129b1",
    "#17defc",
    "#f86363",
];
var borderStartColor = [
    "#0077c5",
    "#a819d7",
    "#c99002",
    "#24bc00",
    "#b6cb04",
    "#112ee2",
    "#00bd9c",
    "#ce078f",
    "#00b2cd",
    "#ec3c3c",
];


//------------广东省寄派件数据内容---------------
//点击筛选按钮
$("#filBtn").on("click", function () {
    if ($("#filCon").is(":hidden")) {
        $("#filCon").attr("style", "display:flex");
    } else {
        $("#filCon").hide();
    }
});
//点击筛选按钮end


$("#switchBtn").on("click", "span", function () {
    $(this).addClass("active").siblings().removeClass("active");
    if ($(this).data("datatype") == "income") {
        $("#totalProfit").html("123,456.5元");
    } else if ($(this).data("datatype") == "expend") {
        $("#totalProfit").html("32,111.4元");
    }
});

$("#tabBtn").on("click", function () {
    var _this = $(this);
    if ($(".right-top").children(".chart-box").is(":hidden")) {
        _this.children("span").html("图表");
        $(".right-top")
            .children(".chart-box")
            .show()
            .siblings(".data-box")
            .hide();
    } else {
        _this.children("span").html("表格");
        $(".right-top")
            .children(".data-box")
            .show()
            .siblings(".chart-box")
            .hide();
        if (_this.data("state") == 1) {
            $(".table1").eq(0).show().siblings("table").hide();
        } else if (_this.data("state") == 2) {
            $(".table1").eq(1).show().siblings("table").hide();
        }
    }
});

$("#tabBtns").on("click", function () {
    var _this = $(this);
    if (_this.siblings(".pop-chart").is(":hidden")) {
        _this.children("span").html("图表");
        _this.siblings(".pop-chart").show().siblings(".data-box").hide();
    } else {
        _this.children("span").html("表格");
        _this.siblings(".data-box").show().siblings(".chart-box").hide();
        if (_this.data("state") == 1) {
            $(".table2").eq(0).show().siblings("table").hide();
        } else if (_this.data("state") == 2) {
            $(".table2").eq(1).show().siblings("table").hide();
        }
    }
});

//时间选择器
var startV = "";
var endV = "";
laydate.skin("danlan");
var startTime = {
    elem: "#startTime",
    format: "YYYY-MM-DD",
    min: "1997-01-01", //设定最小日期为当前日期
    max: laydate.now(), //最大日期
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        startV = datas;
        endTime.min = datas; //开始日选好后，重置结束日的最小日期
    },
};
var endTime = {
    elem: "#endTime",
    format: "YYYY-MM-DD",
    min: laydate.now(),
    max: laydate.now(),
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        endV = datas;
    },
};

laydate(startTime);
laydate(endTime);

//时间选择器
var startVs = "";
var endVs = "";
laydate.skin("danlan");
var startTimes = {
    elem: "#startTimes",
    format: "YYYY-MM-DD",
    min: "1997-01-01", //设定最小日期为当前日期
    max: "2099-06-16", //最大日期
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        startVs = datas;
        endTimes.min = datas; //开始日选好后，重置结束日的最小日期
        setQgData($("#barTypes").parent().parent(), 1);
    },
};
var endTimes = {
    elem: "#endTimes",
    format: "YYYY-MM-DD",
    min: laydate.now(),
    max: laydate.now(),
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        endVs = datas;
        setQgData($("#barTypes").parent().parent(), 1);
    },
};

laydate(startTimes);
laydate(endTimes);

//点击时间选择器的时候更改样式
$("#endTime").on("click", function () {
    dateCss();
});

$("#end").on("click", function () {
    dateCss();
});

//更改日期插件的样式
function dateCss() {
    var arr = $("#laydate_box").attr("style").split(";");
    var cssStr = "position:absolute;right:0;";
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].indexOf("top") != -1) {
            cssStr += arr[i];
        }
    }

    $("#laydate_box").attr("style", cssStr);
}

$(".close-pop").on("click", function () {
    $(this)
        .parent()
        .parent()
        .hide()
        .find(".cont-div")
        .attr("style", "visibility: hidden");
});

$("#setBtn").on("click", function () {
    $(".container")
        .attr("style", "visibility: visible")
        .find(".pop-up")
        .eq(4)
        .attr("style", "visibility: visible")
        .siblings()
        .attr("style", "visibility: hidden");
});

var workDate;
var time = {
    elem: "#times",
    format: "YYYY-MM-DD",
    min: laydate.now(),
    max: laydate.now() + 30,
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        workDate = datas;
    },
};

laydate(time);

$("#addT").on("click", function () {
    $("#mineusT").show();
    if ($(this).siblings("input").length < 6) {
        if ($(this).siblings("input").length == 5) {
            $(this).hide();
        }
        $(this).before('<input type="text" value="">');
    }
});

$("#mineusT").on("click", function () {
    if ($(this).siblings("input").length > 1) {
        if ($(this).siblings("input").length == 6) {
            $("#addT").show();
        } else if ($(this).siblings("input").length == 2) {
            $(this).hide();
        }
        $(this).siblings("input:last").remove();
    }
});

$("#addL").on("click", function () {
    $("#mineusL").show();
    if ($(this).siblings("input").length < 3) {
        if ($(this).siblings("input").length == 2) {
            $(this).hide();
        }
        $(this).before('<input type="text" value="">');
    }
});

$("#mineusL").on("click", function () {
    if ($(this).siblings("input").length > 1) {
        if ($(this).siblings("input").length == 3) {
            $("#addL").show();
        } else if ($(this).siblings("input").length == 2) {
            $(this).hide();
        }
        $(this).siblings("input:last").remove();
    }
});
