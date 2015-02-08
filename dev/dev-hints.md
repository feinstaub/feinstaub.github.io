dev hints for QT, KDE, C++, cmake
=================================

make/cmake/gcc
--------------
* How do I force make/gcc to show me the commands?
  * ```make VERBOSE=1``` or ```make V=1```
* Treat a specific warning as error (e.g. error on missing return statement)
  * see http://stackoverflow.com/questions/3486987/error-on-missing-return-statement
  * CMakeLists.txt:
    * ```add_definitions(“-std=c++11″)```
    * ```set(CMAKE_CXX_FLAGS “${CMAKE_CXX_FLAGS} -Wall -Werror=return-type -fdiagnostics-show-option”)```


kdevelop: header guard snippet
------------------------------
name: hg

Snippet:
```
#ifndef ${g`headerGuard`}
#define ${g}

%{cursor}

#endif // ${g}
```

Scripts:
```
function headerGuard() {
  var filename = document.fileName().toUpperCase();
  filename = filename.replace(/[\.\-]/, '_');
  return filename;
}

function mocHeader() {
  var filename = document.fileName();
  return filename.replace(/.cpp$/, '.moc');
}

function mocImpl() {
  var filename = document.fileName();
  return "moc_" + filename;
}
```
