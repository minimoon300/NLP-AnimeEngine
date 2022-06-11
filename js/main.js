/*  ---------------------------------------------------
    Theme Name: Anime
    Description: Anime video tamplate
    Author: Colorib
    Author URI: https://colorib.com/
    Version: 1.0
    Created: Colorib
---------------------------------------------------------  */

'use strict';

(function ($) {
    /*------------------
        my_algorithm
    --------------------*/
    
    var form = document.getElementById('my-search-model-form')
    
    if (form) {
        form.addEventListener('submit', function(event){
            event.preventDefault()
            
            var search = document.getElementById('search-input').value
            
            console.log(search)
            
            document.location.href = "./search-results.html";
        })
    }
    
    /*------------------
        my_login_and_register
    --------------------*/

    var form = document.getElementById('register-form')
    
    if (form) {
        form.addEventListener('submit', function(event){
            event.preventDefault()
            
            var email = document.getElementById('email-input').value
            var name = document.getElementById('name-input').value
            var password = document.getElementById('password-input').value

            $.ajax({
                type: "POST",
                method: "POST",
                url: "http://127.0.0.1:8080/users",
                crossDomain: true,
                headers: {
                    "content-type": "application/json",
                },
                data: JSON.stringify({ email : email , username : name, password : password}),
                success: function (result) {
                    console.log(result);
                },
                processData: false,
                dataType: "json"
                });
            
            /* console.log(email)
            console.log(name)
            console.log(password) */
            
            document.location.href = "./index.html";
        })
    }

    var form = document.getElementById('login-form')
    
    if (form) {
        form.addEventListener('submit', function(event){
            event.preventDefault()
            
            var email = document.getElementById('email-input').value
            var password = document.getElementById('password-input').value                  
            
            $.ajax({
                type: "POST",
                method: "POST",
                url: "http://127.0.0.1:8080/login",
                crossDomain: true,
                headers: {
                    "content-type": "application/json",
                },
                data: JSON.stringify({ email : email, password : password}),
                success: function (result) {
                    console.log(result);
                },
                processData: false,
                dataType: "json"
                });

            /* console.log(email)
            console.log(password) */
            
            document.location.href = "./index.html";
        })
    }


    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            FIlter
        --------------------*/
        $('.filter__controls li').on('click', function () {
            $('.filter__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.filter__gallery').length > 0) {
            var containerEl = document.querySelector('.filter__gallery');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    // Search model
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
		Hero Slider
	--------------------*/
    var hero_s = $(".hero__slider");
    hero_s.owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        nav: true,
        navText: ["<span class='arrow_carrot-left'></span>", "<span class='arrow_carrot-right'></span>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        mouseDrag: false
    });

    /*------------------
        Video Player
    --------------------*/
    const player = new Plyr('#player', {
        controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'captions', 'settings', 'fullscreen'],
        seekTime: 25
    });

    /*------------------
        Niceselect
    --------------------*/
    $('select').niceSelect();

    /*------------------
        Scroll To Top
    --------------------*/
    $("#scrollToTopButton").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
     });

})(jQuery);