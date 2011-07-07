Name:           w3af
Version:        1.0
Release:        %mkrel 1
Summary:        Web Application Attack and Audit Framework
Group:          Monitoring
License:        GPLv2
URL:            http://w3af.sourceforge.net/
Source0:        http://sourceforge.net/projects/w3af/files/w3af/w3af%201.0-stable/w3af-%{version}-stable.tar.bz2
Requires:       python-pysvn
Requires:       python-nltk
Requires:       python-soap
Requires:       python-numarray
Requires:       scapy
BuildArch:		noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
w3af is a Web Application Attack and Audit Framework. The project's goal is to
create a framework to find and exploit web application vulnerabilities that is
easy to use and extend. To read our short and long term objectives, please
click over the Project Objectives item in the main menu. This project is
currently hosted at SourceForge , for further information, you may also want to
visit w3af SourceForge project page.

%package gui
Summary:    GUI for %{name}
Group:      Monitoring
License:    GPLv2
Requires:   %{name} = %{version}-%{release}
Requires:   python-gtksourceview

%description gui
This is a gui for %{name}.

%prep
%setup -q -n w3af
find . -name .svn | xargs rm -rf

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 w3af_console %{buildroot}%{_datadir}/%{name}
install -m 755 w3af_gui %{buildroot}%{_datadir}/%{name}
cp -pr core %{buildroot}%{_datadir}/%{name}
cp -pr extlib %{buildroot}%{_datadir}/%{name}
cp -pr locales %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr profiles %{buildroot}%{_datadir}/%{name}
cp -pr scripts %{buildroot}%{_datadir}/%{name}
cp -pr tools %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/w3af_console <<EOF
#!/bin/sh

cd %{_datadir}/%{name}
exec ./w3af_console
EOF
chmod +x %{buildroot}%{_bindir}/w3af_console

cat > %{buildroot}%{_bindir}/w3af_gui <<EOF
#!/bin/sh

cd %{_datadir}/%{name}
exec ./w3af_gui
EOF
chmod +x %{buildroot}%{_bindir}/w3af_console

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme/*
%{_datadir}/%{name}
%{_bindir}/w3af_console

%files gui
%defattr(-,root,root)
%{_bindir}/w3af_gui

