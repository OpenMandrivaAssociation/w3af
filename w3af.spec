Name:		w3af
Version:	1.1
Release:	2
Summary:	Web Application Attack and Audit Framework
Group:		Monitoring
License:	GPLv2
URL:		http://w3af.sourceforge.net/
Source0:	http://sourceforge.net/projects/w3af/files/w3af/w3af%201.0-stable/w3af-%{version}.tar.bz2
Patch0:		w3af-fix-python-shellbang.patch
Patch1:		w3af-1.1-add-scriptDir-path.patch
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
%patch0 -p1
%patch1 -p1 
find . -name .svn | xargs rm -rf
rm -f plugins/attack/payloads/code/netcat

%build

%install
install -m755 w3af_console -D %{buildroot}%{_bindir}/w3af_console
install -m755 w3af_gui -D %{buildroot}%{_bindir}/w3af_gui
install -d %{buildroot}%{_datadir}/%{name}
cp -pr core %{buildroot}%{_datadir}/%{name}
cp -pr extlib %{buildroot}%{_datadir}/%{name}
cp -pr locales %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr profiles %{buildroot}%{_datadir}/%{name}
cp -pr scripts %{buildroot}%{_datadir}/%{name}
cp -pr tools %{buildroot}%{_datadir}/%{name}

mv %{buildroot}%{_datadir}/w3af/plugins/discovery/oHalberd/man/ %{buildroot}%{_datadir}/man

%files
%doc readme/CHANGELOG readme/CONTRIBUTORS readme/README readme/TODO
%doc readme/EN
%lang(fr) %doc readme/FR
%lang(ru) %doc readme/RU
%{_datadir}/%{name}
%{_bindir}/w3af_console
%{_mandir}/man1/halberd.1*

%files gui
%{_bindir}/w3af_gui
