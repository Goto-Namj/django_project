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

});