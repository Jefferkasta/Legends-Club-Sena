(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Date and time picker
    $('#date').datetimepicker({
        format: 'L'
    });
    $('#time').datetimepicker({
        format: 'LT'
    });


    // Service carousel
    $(".service-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        loop: true,
        dots: false,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            },
            1200:{
                items:5
            }
        }
    });


    // Pricing carousel
    $(".pricing-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 30,
        loop: true,
        dots: false,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            }
        }
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 30,
        dots: true,
        loop: true,
        items: 1
    });

    // crea super Usuario
    $("#btn-register-admin").on('click', function(e) {
        e.preventDefault();
        // setTimeout(function() { 
        //     $('#messageUser').fadeOut();}, 2000); 
        let formAdmin = new FormData(formNewAdmin);
        let useremail = [formAdmin.get('txt-useremail')];
        let userfirstname = [formAdmin.get('txt-userfirstname')];
        let userlastname = [formAdmin.get('txt-userlastname')];
        let userage = [formAdmin.get('txt-userage')];
        let userphone = [formAdmin.get('txt-userphone')];
        let passwlogin = [formAdmin.get('txt-passwlogin')];
        let confirmpasswlogin = [formAdmin.get('txt-confirmpasswlogin')];

        var admin = {
            csrfmiddlewaretoken:formAdmin.get('csrfmiddlewaretoken'),
            useremail,
            userfirstname,
            userlastname,
            userage, 
            userphone, 
            passwlogin,
            confirmpasswlogin
        }

        $.ajax({
            type: "POST",
            url: 'new-superuser/',
            data: admin,
            // headers: { 'X-CSRF-TOKEN': formAdmin.get('csrfmiddlewaretoken') }
        }).done(function(e){
            let modal = $('#modal-nuevoAdmin');
            modal.modal('hide');
            modal.css('display','none');
            modal.removeClass('show');
            modal.removeAttr('aria-modal');
            modal.attr('aria-hidden="true"');
            // $("messageUser").removeClass('success');
            // setTimeout(() => {
            //     $("messageUser").addClass('success');
            // }, 2000);
        });
    });

    // crea Artista
    $("#btn-register-artista").on('click', function(e) {
        e.preventDefault();
        // setTimeout(function() { 
        //     $('#messageUser').fadeOut();}, 2000); 
        let formAdmin = new FormData(formNewArtista);
        let artistidentification = [formAdmin.get('txt-artistidentification')];
        let artistestile = [formAdmin.get('txt-artistestile')];
        let artistexperience = [formAdmin.get('txt-artistexperience')];
        let artistnationality = [formAdmin.get('txt-artistnationality')];

        var artist = {
            csrfmiddlewaretoken:formAdmin.get('csrfmiddlewaretoken'),
            artistidentification,
            artistestile,
            artistexperience,
            artistnationality
        }
        console.log(artist);
        //crear artist
        $.ajax({
            type: "POST",
            url: 'new-artista/',
            data: artist,
            // headers: { 'X-CSRF-TOKEN': formAdmin.get('csrfmiddlewaretoken') }
        }).done(function(e){
            let modal = $('#modal-nuevoAdmin');
            modal.modal('hide');
            modal.css('display','none');
            modal.removeClass('show');
            modal.removeAttr('aria-modal');
            modal.attr('aria-hidden="true"');
            // $("messageUser").removeClass('success');
            // setTimeout(() => {
            //     $("messageUser").addClass('success');
            // }, 2000);
        });
    });

    
})(jQuery);

