#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <string>
using namespace std;

MainWindow::MainWindow(QWidget *parent): QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

/**********************************************************************************************************************************************************************/

    QFont applicationHeaderFontProperties;
    applicationHeaderFontProperties.setBold(true);
    applicationHeaderFontProperties.setCapitalization(QFont::Capitalization(QFont::AllUppercase));
    applicationHeaderFontProperties.setUnderline(true);
    applicationHeaderFontProperties.setPixelSize(40);
    this->ui->Application_Header->setFont(applicationHeaderFontProperties);

    QString applicationHeaderLabelName = "FTP Application";
    this->ui->Application_Header->setText(applicationHeaderLabelName);

    /*********************DEBUG**************************************************************************************/

    qDebug() << "Application Header Pixel Size = " << applicationHeaderFontProperties.pixelSize() << " px.";
    qDebug() << "Application Header Text has " << applicationHeaderLabelName.size() << " letters.";
    qDebug() << "Application Header Bold? = " << applicationHeaderFontProperties.bold() << endl;

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont hostNameFontProperties;
    hostNameFontProperties.setBold(false);
    hostNameFontProperties.setCapitalization(QFont::Capitalization(QFont::AllUppercase));
    hostNameFontProperties.setPixelSize(30);
    this->ui->host_Label->setFont(hostNameFontProperties);

    QString hostLabelName = "HOST/IP:";
    this->ui->host_Label->setText(hostLabelName);

    /*********************DEBUG***************************************************************************************/

    qDebug() << "Host Label Pixel Size = " << hostNameFontProperties.pixelSize() << "px";
    qDebug() << "Host Label Bold? = " << hostNameFontProperties.bold() << endl;

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont idNameFontProperties;
    idNameFontProperties.setBold(false);
    idNameFontProperties.setCapitalization(QFont::Capitalization(QFont::AllUppercase));
    idNameFontProperties.setPixelSize(30);
    this->ui->id_Label->setFont(idNameFontProperties);

    QString idLabelName = "ID:";
    this->ui->id_Label->setText(idLabelName);


    /*********************DEBUG***************************************************************************************/

    qDebug() << "ID Label Pixel Size = " << idNameFontProperties.pixelSize() << "px";
    qDebug() << "ID Label Bold? = " << idNameFontProperties.bold() << endl;

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont passwordFontProperties;
    passwordFontProperties.setBold(false);
    passwordFontProperties.setCapitalization(QFont::Capitalization(QFont::AllUppercase));
    passwordFontProperties.setPixelSize(23);
    this->ui->password_Label->setFont(passwordFontProperties);


    QString passwordLabelName = "Password:";
    this->ui->password_Label->setText(passwordLabelName);


    /*********************DEBUG***************************************************************************************/

    qDebug() << "Password Label Pixel Size = " << passwordFontProperties.pixelSize() << "px";
    qDebug() << "Password Label Bold? = " << passwordFontProperties.bold() << endl;

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont portFontProperties;
    portFontProperties.setBold(false);
    portFontProperties.setCapitalization(QFont::Capitalization(QFont::AllUppercase));
    portFontProperties.setPixelSize(30);
    this->ui->port_Label->setFont(portFontProperties);

    QString portLabelName = "Port:";
    this->ui->port_Label->setText(portLabelName);

    this->ui->port_Label->setGeometry(360,370,81,51);

    /*********************DEBUG***************************************************************************************/

    qDebug() << "Port Label Pixel Size = " << portFontProperties.pixelSize() << "px";
    qDebug() << "Port Label Bold? = " << portFontProperties.bold() << endl;

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont hostTextInputFontProperties;
    hostTextInputFontProperties.setPixelSize(25);
    this->ui->textInput_Host->setFont(hostTextInputFontProperties);

    //QString hostTextInputDefaultLabelName = "127.0.0.1";
    //this->ui->textInput_Host->setText(hostTextInputDefaultLabelName);

    QString hostTextInputFromUser = this->ui->textInput_Host->text();

    /*********************DEBUG***************************************************************************************/

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont idTextInputFontProperties;
    idTextInputFontProperties.setPixelSize(25);
    this->ui->textInput_ID->setFont(idTextInputFontProperties);

    QString idTextInputDefaultLabelName = "username";
    this->ui->textInput_ID->setText(idTextInputDefaultLabelName);

    /*********************DEBUG***************************************************************************************/

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

    QFont passwordTextInputFontProperties;
    passwordTextInputFontProperties.setPixelSize(25);
    this->ui->textInput_Password->setFont(passwordTextInputFontProperties);

    //QString passwordTextInputDefaultLabelName = "**********";
    //this->ui->textInput_Password->setText(passwordTextInputDefaultLabelName);
    this->ui->textInput_Password->setEchoMode(QLineEdit::Password);

    /*********************DEBUG***************************************************************************************/

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

     QFont portTextInputFontProperties;
     portTextInputFontProperties.setPixelSize(25);
     this->ui->textInput_Port->setFont(portTextInputFontProperties);

     QString portTextInputDefaultLabelName = "22";
     this->ui->textInput_Port->setText(portTextInputDefaultLabelName);
     //this->ui->textInput_Port->setFixedSize(100,40);
     this->ui->textInput_Port->setGeometry(490,375,100,45);

     /*********************DEBUG***************************************************************************************/

    /*********************DEBUG***************************************************************************************/

/**********************************************************************************************************************************************************************/

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_textInput_Host_textChanged(const QString &arg1)
{
    static bool didUserChangeHostTextInput = false;
    if(didUserChangeHostTextInput == false)
    {
        this->ui->progressBar->setValue(this->ui->progressBar->value() + 25);
        didUserChangeHostTextInput = true;
    }

}
