%define		plugin	gmic

Summary:	G'MIC interpreter embedded in a GIMP plug-in
Name:		gimp-plugin-%{plugin}
Version:	1.6.3.1
Release:	1
License:	CeCILL FREE SOFTWARE LICENSE
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/sourceforge/gmic/%{plugin}_%{version}.tar.gz
# Source0-md5:	90c85c90953d928be0bf689403da553e
BuildRequires:	fftw3-devel
BuildRequires:	gimp-devel
BuildRequires:	libstdc++-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool-2.0 --gimpplugindir)/plug-ins

%description
G'MIC interpreter embedded in a GIMP plug-in.

%prep
%setup -qn %{plugin}-%{version}

%{__sed} -i '/strip\ gmic.*/d' src/Makefile

%build
%{__make} -j1 -C src gimp		\
	CC="%{__cxx}"			\
	OPT_CFLAGS="%{rpmldflags} %{rpmcxxflags} -fno-ipa-sra"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}

install -D src/gmic_gimp $RPM_BUILD_ROOT%{plugindir}/gmic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{plugindir}/gmic

