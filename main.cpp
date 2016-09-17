#include "mainwindow.h"
<<<<<<< HEAD
=======
#include "qtftp/src/qftp/qftp.h"
#include "qtftp/src/qftp/qurlinfo.h"

#include <QObject>
>>>>>>> 30b3f4576b6fd7563c04134f6950e6e6b6baefe2
#include <QApplication>
#include <QDebug>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.show();

    return a.exec();
}
