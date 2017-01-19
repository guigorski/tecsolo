/*
 99Lime.com HTML KickStart by Joshua Gatcke
 kickstart.js
 */

jQuery(document).ready(function ($) {



    /*---------------------------------
     Image Caption
     -----------------------------------*/
    $('img.caption').each(function () {
        $(this).wrap('<div class="caption">');
        $(this).parents('div.caption')
                .attr('class', 'img-wrap ' + $(this).attr('class'));
        if ($(this).attr('title')) {
            $(this).parents('div.caption')
                    .append('<span>' + $(this).attr('title') + '</span>');
        }
    });


    /*---------------------------------
     CSS Helpers
     -----------------------------------*/
    $('input[type=checkbox]').addClass('checkbox');
    $('input[type=radio]').addClass('radio');
    $('input[type=file]').addClass('file');
    $('[disabled=disabled]').addClass('disabled');
    $('table').find('tr:even').addClass('alt');
    $('table').find('tr:first-child').addClass('first');
    $('table').find('tr:last-child').addClass('last');
    $('ul').find('li:first-child').addClass('first');
    $('ul').find('li:last-child').addClass('last');
    $('hr').before('<div class="clear">&nbsp;</div>');
    $('[class*="col_"]').addClass('column');
    $('pre').addClass('prettyprint');
    prettyPrint();

});

$('.form').find('input, textarea').on('keyup blur focus', function (e) {

    var $this = $(this),
            label = $this.prev('label');

    if (e.type === 'keyup') {
        if ($this.val() === '') {
            label.removeClass('active highlight');
        } else {
            label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
        if ($this.val() === '') {
            label.removeClass('active highlight');
        } else {
            label.removeClass('highlight');
        }
    } else if (e.type === 'focus') {

        if ($this.val() === '') {
            label.removeClass('highlight');
        } else if ($this.val() !== '') {
            label.addClass('highlight');
        }
    }

});

$('.tab a').on('click', function (e) {

    e.preventDefault();

    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');

    target = $(this).attr('href');

    $('.tab-content > div').not(target).hide();

    $(target).fadeIn(600);

});
