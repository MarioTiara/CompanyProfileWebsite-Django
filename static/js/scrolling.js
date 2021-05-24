$(window).scroll(function(){
    var scroll=$(window).scrollTop();
    

    if (scroll>=200){
        $("#myNav").addClass("bg-white");
        $("#about").addClass("text-dark");
        $("#services").addClass("text-dark");
        $("#portofolio").addClass("text-dark");
    }
    else {
        $("#myNav").removeClass("bg-white");
        $("#about").removeClass("text-dark");
        $("#services").removeClass("text-dark");
        $("#portofolio").removeClass("text-dark");
        
    }
})