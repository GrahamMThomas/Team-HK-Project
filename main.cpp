#include "mainwindow.h"
#include "qtftp/src/qftp/qftp.h"
#include "qtftp/src/qftp/qurlinfo.h"

#include <QObject>
#include <QApplication>
#include <QDebug>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.show();

    return a.exec();
}
