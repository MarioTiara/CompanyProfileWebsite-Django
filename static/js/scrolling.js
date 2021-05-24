$(window).scroll(function(){
    var scroll=$(window).scrollTop();
    
    if (scroll>=200){
        $("#myNav").addClass("bg-dark");
        $("#about").addClass("text-white");
        $("#services").addClass("text-white");
        $("#portofolio").addClass("text-white");
    }
    else {
        $("#myNav").removeClass("bg-dark");
        $("#about").removeClass("text-white");
        $("#services").removeClass("text-white");
        $("#portofolio").removeClass("text-white");
        
    }
    
})