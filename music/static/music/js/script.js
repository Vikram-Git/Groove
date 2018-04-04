function favArtist(){
    var target = $(".artist-container .btn-fav");

    target.on("click", function(e){
        e.preventDefault();

        var self = $(this);
        var url = $(this).attr('href');

        $.getJSON(url, function(result){
            if (result.success){
                $("i", self).toggleClass("favourite");
            }
        });
        return false;
    });
};


function favSong(){
    var target = $(".song-container .btn-fav");

    target.on("click", function(e){
        e.preventDefault();

        var self = $(this);
        var url = $(this).attr("href");
        $.getJSON(url, function(result){
            if (result.success){
                $("i", self).toggleClass('favourite');
            };
        return false;
        });
    });
};

function deleteSong(){

    var target = $(".song-container .btn-delete");

    target.on("click", function(e){
        e.preventDefault();
        var self = $(this);
        var url = $(this).attr("href");
        $.getJSON(url, function(result){
            if (result.success){
                location.reload();
        };
        return false;
        });
    });
};

$(document).ready(function(){
    favArtist();
    favSong();
    deleteSong()
});
