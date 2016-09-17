/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTimeEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *id_Label;
    QLabel *password_Label;
    QLabel *Application_Header;
    QDateEdit *dateEdit;
    QLabel *host_Label;
    QTimeEdit *timeEdit;
    QPushButton *connect_PushButton;
    QProgressBar *progressBar;
    QLabel *port_Label;
    QLineEdit *textInput_Host;
    QLineEdit *textInput_ID;
    QLineEdit *textInput_Password;
    QLineEdit *textInput_Port;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1135, 641);
        MainWindow->setAutoFillBackground(true);
        MainWindow->setTabShape(QTabWidget::Triangular);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        id_Label = new QLabel(centralWidget);
        id_Label->setObjectName(QStringLiteral("id_Label"));
        id_Label->setGeometry(QRect(430, 230, 51, 51));
        QFont font;
        font.setFamily(QStringLiteral("DFKai-SB"));
        font.setPointSize(22);
        font.setBold(true);
        font.setWeight(75);
        id_Label->setFont(font);
        password_Label = new QLabel(centralWidget);
        password_Label->setObjectName(QStringLiteral("password_Label"));
        password_Label->setGeometry(QRect(340, 310, 141, 51));
        password_Label->setFont(font);
        password_Label->setInputMethodHints(Qt::ImhNone);
        Application_Header = new QLabel(centralWidget);
        Application_Header->setObjectName(QStringLiteral("Application_Header"));
        Application_Header->setGeometry(QRect(390, 50, 401, 51));
        QFont font1;
        font1.setFamily(QStringLiteral("Maiandra GD"));
        font1.setPointSize(36);
        font1.setBold(false);
        font1.setItalic(false);
        font1.setWeight(50);
        Application_Header->setFont(font1);
        dateEdit = new QDateEdit(centralWidget);
        dateEdit->setObjectName(QStringLiteral("dateEdit"));
        dateEdit->setGeometry(QRect(980, 480, 151, 41));
        QFont font2;
        font2.setFamily(QStringLiteral("Franklin Gothic Demi"));
        font2.setPointSize(16);
        font2.setUnderline(true);
        dateEdit->setFont(font2);
        dateEdit->setDateTime(QDateTime(QDate(2016, 9, 17), QTime(3, 24, 30)));
        dateEdit->setCurrentSection(QDateTimeEdit::MonthSection);
        dateEdit->setCalendarPopup(true);
        dateEdit->setTimeSpec(Qt::UTC);
        host_Label = new QLabel(centralWidget);
        host_Label->setObjectName(QStringLiteral("host_Label"));
        host_Label->setGeometry(QRect(350, 160, 131, 51));
        host_Label->setFont(font);
        timeEdit = new QTimeEdit(centralWidget);
        timeEdit->setObjectName(QStringLiteral("timeEdit"));
        timeEdit->setGeometry(QRect(980, 530, 151, 41));
        QFont font3;
        font3.setFamily(QStringLiteral("Franklin Gothic Book"));
        font3.setPointSize(16);
        font3.setBold(true);
        font3.setWeight(75);
        timeEdit->setFont(font3);
        timeEdit->setDateTime(QDateTime(QDate(2016, 9, 15), QTime(9, 41, 20)));
        connect_PushButton = new QPushButton(centralWidget);
        connect_PushButton->setObjectName(QStringLiteral("connect_PushButton"));
        connect_PushButton->setGeometry(QRect(310, 440, 461, 41));
        QFont font4;
        font4.setFamily(QStringLiteral("Franklin Gothic Book"));
        font4.setPointSize(20);
        connect_PushButton->setFont(font4);
        connect_PushButton->setCheckable(true);
        progressBar = new QProgressBar(centralWidget);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setGeometry(QRect(310, 480, 471, 23));
        QPalette palette;
        QBrush brush(QColor(255, 0, 0, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        QBrush brush1(QColor(120, 120, 120, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush1);
        progressBar->setPalette(palette);
        QFont font5;
        font5.setPointSize(16);
        progressBar->setFont(font5);
        progressBar->setValue(20);
        port_Label = new QLabel(centralWidget);
        port_Label->setObjectName(QStringLiteral("port_Label"));
        port_Label->setGeometry(QRect(390, 370, 81, 51));
        port_Label->setFont(font);
        port_Label->setInputMethodHints(Qt::ImhNone);
        textInput_Host = new QLineEdit(centralWidget);
        textInput_Host->setObjectName(QStringLiteral("textInput_Host"));
        textInput_Host->setGeometry(QRect(490, 170, 281, 41));
        textInput_ID = new QLineEdit(centralWidget);
        textInput_ID->setObjectName(QStringLiteral("textInput_ID"));
        textInput_ID->setGeometry(QRect(500, 250, 271, 41));
        textInput_Password = new QLineEdit(centralWidget);
        textInput_Password->setObjectName(QStringLiteral("textInput_Password"));
        textInput_Password->setGeometry(QRect(490, 320, 261, 41));
        textInput_Port = new QLineEdit(centralWidget);
        textInput_Port->setObjectName(QStringLiteral("textInput_Port"));
        textInput_Port->setGeometry(QRect(470, 380, 281, 41));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1135, 21));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        id_Label->setText(QApplication::translate("MainWindow", "ID:", 0));
        password_Label->setText(QApplication::translate("MainWindow", "PASSWORD: ", 0));
        Application_Header->setText(QApplication::translate("MainWindow", "FTP Application ", 0));
        host_Label->setText(QApplication::translate("MainWindow", "HOST/IP:", 0));
        connect_PushButton->setText(QApplication::translate("MainWindow", "CONNECT", 0));
        port_Label->setText(QApplication::translate("MainWindow", "PORT:", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
