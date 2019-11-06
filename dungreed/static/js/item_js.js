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
    var clicked;
    $(chd$).click(function() {
        clicked = event.target.className;
        $(".pd3").children().css("display","none");
        $(".item_list_pd").children().removeClass('item_element_choose');
        $("."+clicked+"_detail").css("display","block");
        $("."+clicked+"_choose").addClass('item_element_choose');
    });

    $(chd$).mouseenter(function() {
        if(clicked!=event.target.className){
            $("."+event.target.className+"_choose").addClass('item_element_choose');
        }
    });

    $(chd$).mouseleave(function() {
        if(clicked!=event.target.className){
            $("."+event.target.className+"_choose").removeClass('item_element_choose');
        }
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
    $("#ipt1").val(vl1);
    $("#ipt2").val(vl2);
    $("#slider").slider({
        range: true,
        values: [vl1,vl2],
        step: stepv,
        min: minv,
        max: maxv,
        slide: function( event, ui ) {
            $("#ipt1").val(ui.values[0]);
            vl1 = ui.values[0];
            $("#ipt2").val(ui.values[1]);
            vl2 = ui.values[1];
        }
    });
    $("#ipt1").change(function() {
        var value1 = this.value;
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
        $("#ipt1").val(vl1);
        $("#slider").slider("values", [vl1,vl2]);
    });
    $("#ipt2").change(function() {
        var value2 = this.value;
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
        $("#ipt2").val(vl2);
        $("#slider").slider("values", [vl1,vl2]);
    });

    $(".ordbtn").click(function() {
        $order("item_list","item_element");
    });

    $order = function(li, bb) {
        var list, i, switching, b, shouldSwitch, dir, switchcount = 0;
        list = document.getElementsByClassName(li)[0];
        switching = true;
        dir = "asc"; 
        while (switching) {
            switching = false;
            b = list.getElementsByClassName(bb);
            for (i = 0; i < (b.length - 1); i++) {
                shouldSwitch = false;
                if (dir == "asc") {
                    if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        $('.ordbtn').text('△');
                        break;
                    }
                } else if (dir == "desc") {
                    if (b[i].innerHTML.toLowerCase() < b[i + 1].innerHTML.toLowerCase()) {
                        shouldSwitch= true;
                        $('.ordbtn').text('▽');
                        break;
                    }
                }
            }
            if (shouldSwitch) {
                b[i].parentNode.insertBefore(b[i + 1], b[i]);
                switching = true;
                switchcount ++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    }

    $(document).on('mouseenter', '.nowfilter', function() {
        $("#"+event.target.id).css("background-color","#a54bff");});
    $(document).on('mouseleave', '.nowfilter', function() {
        $("#"+event.target.id).css("background-color","#a97874");});
    $(document).on('mouseenter', '.everyfilter', function() {
        $('.everyfilter').css("background-color","#477eff");});
    $(document).on('mouseleave', '.everyfilter', function() {
        $('.everyfilter').css("background-color","#654a59");});
});