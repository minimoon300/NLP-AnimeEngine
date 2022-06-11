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
        my_anime-search-list
    --------------------*/

    function createAnimeSearchList(id, name, image_link, score, rank, members) {
        var elem = `<div class="col-lg-4 col-md-6 col-sm-6">` +
                    `<div class="product__item">` +
                        `<div class="product__item__pic set-bg" data-setbg="${image_link}" style="background-image: url('${image_link}');">` +
                            `<div class="ep">${score} / 10</div>` +
                            `<div class="comment"><i class="fa fa-star"></i> ${Math.trunc(rank)}</div>` +
                            `<div class="view"><i class="fa fa-eye"></i> ${members}</div>` +
                        `</div>` +
                        `<div class="product__item__text">` +
                            `<ul>` +
                                `<li>Active</li>` +
                                `<li>Movie</li>` +
                            `</ul>` +
                            `<h5><a href="./anime-info-page.html?id=${id}">${name}</a></h5>` +
                        `</div>` +
                    `</div>` +
                `</div>`;

        return elem;
    }

    $( document ).ready(function() {
        if ($('#anime-search-list').length) {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:8080/animes",
                success: function (result) {
                    var anime_list = result;
                    for (var i = 0; i < 21; i++) {
                        $('#anime-search-list').append(createAnimeSearchList(i, result[i]["title"], result[i]["img_url"], result[i]["score"], result[i]["ranked"], result[i]["members"]));
                      }
                },
                dataType: "json"
                });
        }
    });

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