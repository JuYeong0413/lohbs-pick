 // Accordion        
 $(".accordion").each(function(){
    var allPanels = $(this).children("dd").hide();
    $(this).children("dd").first().slideDown("easeOutExpo");
    $(this).children("dt").children("a").first().addClass("active");
                
    $(this).children("dt").children("a").click(function(){        
        var current = $(this).parent().next("dd");
        $(".accordion > dt > a").removeClass("active");
        $(this).addClass("active");
        allPanels.not(current).slideUp("easeInExpo");
        $(this).parent().next().slideDown("easeOutExpo");                
        return false;                
    });
    
 });