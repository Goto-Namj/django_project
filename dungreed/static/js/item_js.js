$(document).ready(function() {
    var $bodyOffset = $('body').offset();
    $(window).scroll(function() {
        if ($(document).scrollTop() > $bodyOffset.top+198) {
            $('.item_detail').addClass('scroll');
        } else {
            $('.item_detail').removeClass('scroll');
        }
    });


    var chd$ = $('.item_element').children();
    $(chd$).click(function(){
        $(".pd3").children().css("display","none");
        $(".item_list_pd").children().removeClass('item_element_choose');
        $("."+event.target.className+"_detail").css("display","block");
        $("."+event.target.className+"_choose").addClass('item_element_choose');
    });


    //공격력 0(닭다리)~100(각목) 소수점있지만 step=1
    //방어력 1 ~ 20
    //공격속도 0.5~ 21.74 step>=0.1정도
    //탄창 1 ~ 100
    var stepv = 1;
    var minv = 0;
    var maxv = 100;
    var vl1 = minv;
    var vl2 = maxv;
    $("#ipt1").val("$" + vl1);
    $("#ipt2").val("$" + vl2);
    $("#slider").slider({
        range: true,
        values: [vl1,vl2],
        step: stepv,
        min: minv,
        max: maxv,
        slide: function( event, ui ) {
            $("#ipt1").val("$" + ui.values[0]);
            vl1 = ui.values[0];
            $("#ipt2").val("$" + ui.values[1]);
            vl2 = ui.values[1];
        }
    });
    $("#ipt1").change(function () {
        var value1 = this.value.substring(1);
        vl1 = parseFloat(value1);
        if (vl1 < minv) {
            vl1 = minv;
        } else if (vl1 <= vl2) {
            //pass
        } else if (vl1 > vl2) {
            vl1 = vl2;
        } else {
            vl1 = minv;
        }
        $("#ipt1").val("$" + vl1);
        $("#slider").slider("values", [vl1,vl2]);
    });
    $("#ipt2").change(function () {
        var value2 = this.value.substring(1);
        vl2 = parseFloat(value2);
        if (vl2 > maxv) {
            vl2 = maxv;
        } else if (vl1 <= vl2) {
            //pass
        } else if (vl1 > vl2) {
            vl2 = vl1;
        } else {
            vl2 = maxv;
        }
        $("#ipt2").val("$" + vl2);
        $("#slider").slider("values", [vl1,vl2]);
    });

    

});
function myFunction() {
    var x = document.createElement("BUTTON");
    var t = document.createTextNode("Click me");
    x.appendChild(t);
    document.body.appendChild(x);
}