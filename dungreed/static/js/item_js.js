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


    var vl1 = 0;
    var vl2 = 100;
    $("#slider").slider({
        range: true,
        values: [vl1,vl2],
        step: 1,
        min: 0,
        max: 100,
        slide: function( event, ui ) {
            $( "#ipt1" ).val( "$" + ui.values[0] );
            $( "#ipt2" ).val( "$" + ui.values[1] );
        }
    });
    
    $("#ipt1").change(function () {
        var value1 = this.value.substring(1);
        vl1 = parseInt(value1);
        $("#slider").slider("values", [vl1,vl2]);
    });

    $("#ipt2").change(function () {
        var value2 = this.value.substring(1);
        vl2 = parseInt(value2);
        $("#slider").slider("values", [vl1,vl2]);
    });
});