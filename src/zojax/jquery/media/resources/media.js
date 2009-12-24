$(document).ready(function(){
    var portal_url = document.getElementsByTagName('head')[0].attributes['portal'].value;
    $.fn.media.defaults.flvPlayer =  portal_url + '@@/jquery-media/flowplayer-3.1.5.swf';
    $.fn.media.defaults.mp3Player = portal_url + '@@/jquery-media/mediaplayer.swf';
    $.fn.media.defaults.flashvars =  {'plugins': '{ audio: { url: \'flowplayer.audio-3.1.2.swf\'} }'};
    $.fn.media.defaults.bgColor = 'transparent';
    $.fn.media.defaults.types = [];
    for (var i in $.fn.media.defaults.players) {
	$.fn.media.defaults.types = $.fn.media.defaults.types.concat($.fn.media.defaults.players[i].types.split(','))
    };
    $.fn.media.defaults.types.sort();
  
    var old = $.fn.media.flv
    $.fn.media.flv = $.fn.media.mp3 = function(el, opts) {
        var src = opts.src;
        if (opts.type == 'mp3') {
            opts.src = /\?/i.test(src) ? src + '&jquery.media.name=name.mp3' : src + '?jquery.media.name=name.mp3';
            opts.height = '18';
        }
        return old(el, opts)
    }
    
    $('a.z-media').media();
});
