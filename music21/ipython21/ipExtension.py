import music21.ipython21.objects
import os

_DOC_IGNORE_MODULE_OR_PACKAGE = True

def returnDataFromIPython21Object(obj):
    fp = obj.fp
    data = open(fp).read()
    os.remove(fp)
    return data

def load_ipython_extension(ip):
    pngFormatter = ip.display_formatter.formatters['image/png']
    pngFormatter.for_type(music21.ipython21.objects.IPythonPNGObject, returnDataFromIPython21Object)  
    from IPython.display import display, HTML
    display(HTML('''
     <script>
    require.config(
       { baseUrl: "http://web.mit.edu/music21/music21j/src/",
         paths: {'music21': 'http://web.mit.edu/music21/music21j/src/music21',}
        });
    require(['music21'], function () {
          var n = new music21.note.Note("D#4");
          var s = new music21.stream.Stream();
          s.append(n);
          console.log('music21 loaded fine');
    });
    </script>
    '''))