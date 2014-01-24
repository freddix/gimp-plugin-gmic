%define		plugin	gmic

Summary:	G'MIC interpreter embedded in a GIMP plug-in
Name:		gimp-plugin-%{plugin}
Version:	1.5.8.2
Release:	1
License:	CeCILL FREE SOFTWARE LICENSE
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/sourceforge/gmic/%{plugin}_%{version}.tar.gz
# Source0-md5:	3b96d8369a6b91baf13490234b3dcd7c
Patch0:		%{name}-build.patch
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
%patch0 -p1

%build
%{__make} -j1 -C src gimp		\
	CC="%{__cxx}"			\
	OPTCXXFLAGS="%{rpmcxxflags}"	\
	OPTLDFLAGS="%{rpmldflags}"

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

