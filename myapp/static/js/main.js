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
            let modal = $('#modal-newAdmin');
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
            url: 'new-artist/',
            data: artist,
            // headers: { 'X-CSRF-TOKEN': formAdmin.get('csrfmiddlewaretoken') }
        }).done(function(e){
            console.log(e);
            let modal = $('#modal-newArtist');
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

    // crea cita
    $("#btn-register-appointment").on('click', function(e) {
        e.preventDefault();
        // setTimeout(function() { 
        //     $('#messageUser').fadeOut();}, 2000); 
        let formAppointment = new FormData(formNewAppointment);
        let useridentification = [formAppointment.get('txt-useridentification')];
        let idartist = [formAppointment.get('txt-idartist')];
        let timeappointment = [formAppointment.get('txt-timeappointment')];
        let descriptionappointment = [formAppointment.get('txt-descriptionappointment')];
        if(useridentification == '' || idartist == '' || timeappointment == '' || descriptionappointment == ''){
            let modal = $('#contentModal-appointment');
            let alert = $('#alertAppointment');

            alert.css('display','block');
            setTimeout(() => {
                alert.css('display','none');
            }, 2000);
        }else{
            var appointment = {
                csrfmiddlewaretoken:formAppointment.get('csrfmiddlewaretoken'),
                useridentification,
                idartist,
                timeappointment,
                descriptionappointment
            }
            //crear artist
            $.ajax({
                type: "POST",
                url: 'new-appointment/',
                data: appointment,
                // headers: { 'X-CSRF-TOKEN': formAppointment.get('csrfmiddlewaretoken') }
            }).done(function(e){
                console.log(e);
                let modal = $('#modal-newAppointment');
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
        }
        
    });
    // crea articulo
    $("#btn-register-article").on('click', function(e) {
        e.preventDefault();
        // setTimeout(function() { 
        //     $('#messageUser').fadeOut();}, 2000); 
        let formArticle = new FormData(formNewArticle);
        let imageArticle = [formArticle.get('file-imageArticle')];
        let nameArticle = [formArticle.get('txt-nameArticle')];
        let categoryArticle = [formArticle.get('txt-categoryArticle')];
        let descriptionArticle = [formArticle.get('txt-descriptionArticle')];
        let priceArticle = [formArticle.get('txt-priceArticle')];
        if(imageArticle == '' || nameArticle == '' || categoryArticle == '' || descriptionArticle == '', priceArticle == ''){
            let modal = $('#contentModal-article');
            let alert = $('#alertArticle');

            alert.css('display','block');
            setTimeout(() => {
                alert.css('display','none');
            }, 2000);
        }else{
            var article = {
                csrfmiddlewaretoken:formArticle.get('csrfmiddlewaretoken'),
                imageArticle,
                nameArticle,
                categoryArticle,
                descriptionArticle,
                priceArticle
            }
            console.log(article)
            //crear article
            
            $.ajax({
                type: "POST",
                url: 'new-article/',
                data: article,
                // headers: { 'X-CSRF-TOKEN': formAppointment.get('csrfmiddlewaretoken') }
            }).done(function(e){
                console.log(e);
                let modal = $('#modal-newArticle');
                modal.modal('hide');
                modal.css('display','none');
                modal.removeClass('show');
                modal.removeAttr('aria-modal');
                modal.attr('aria-hidden="true"');
                // $("messageUser").removeClass('success');
                // setTimeout(() => {
                //     $("messageUser").addClass('success');
                // }, 2000);
            }).fail(function(jqXHR, textStatus, errorThrown) {
                console.log('Error en la solicitud AJAX:', errorThrown);
            });
           
        }
        
    });

    
})(jQuery);

