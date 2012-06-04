Name:		w3af
Version:	1.1
Release:	2
Summary:	Web Application Attack and Audit Framework
Group:		Monitoring
License:	GPLv2
URL:		http://w3af.sourceforge.net/
Source0:	http://sourceforge.net/projects/w3af/files/w3af/w3af%201.0-stable/w3af-%{version}.tar.bz2
Patch0:		w3af-fix-python-shellbang.patch
Requires:	python-pysvn
Requires:	python-nltk
Requires:	python-soap
Requires:	python-numarray
Requires:	scapy
BuildArch:	noarch

%description
w3af is a Web Application Attack and Audit Framework. The project's goal is to
create a framework to find and exploit web application vulnerabilities that is
easy to use and extend. To read our short and long term objectives, please
click over the Project Objectives item in the main menu. This project is
currently hosted at SourceForge , for further information, you may also want to
visit w3af SourceForge project page.

%package	gui
Summary:	GUI for %{name}
Group:		Monitoring
License:	GPLv2
Requires:	%{name} = %{EVRD}
Requires:	python-gtksourceview

%description	gui
This is a gui for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .shellbang~
find . -name .svn | xargs rm -rf

%build
cat > w3af_console.wrapper <<EOF
#!/bin/sh

cd %{_datadir}/%{name}
exec ./w3af_console
EOF
chmod +x w3af_console

cat > w3af_gui.wrapper <<EOF
#!/bin/sh

cd %{_datadir}/%{name}
exec ./w3af_gui
EOF
chmod +x w3af_gui.wrapper

%install
install -m755 w3af_console -D %{buildroot}%{_datadir}/%{name}/w3af_console
install -m755 w3af_gui -D %{buildroot}%{_datadir}/%{name}/w3af_gui
cp -pr core %{buildroot}%{_datadir}/%{name}
cp -pr extlib %{buildroot}%{_datadir}/%{name}
cp -pr locales %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr profiles %{buildroot}%{_datadir}/%{name}
cp -pr scripts %{buildroot}%{_datadir}/%{name}
cp -pr tools %{buildroot}%{_datadir}/%{name}

install -m755 w3af_console.wrapper -D %{buildroot}%{_bindir}/w3af_console
install -m755 w3af_gui.wrapper -D %{buildroot}%{_bindir}/w3af_gui

%files
%doc readme/*
%{_datadir}/%{name}
%{_bindir}/w3af_console

%files gui
%{_bindir}/w3af_gui
