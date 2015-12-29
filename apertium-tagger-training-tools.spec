Summary:	Apertium part-of-speech tagger trainer
Summary(pl.UTF-8):	Narzędzie Apertium do nauki rozpoznawania części mowy
Name:		apertium-tagger-training-tools
Version:	1.1.1
Release:	0.1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	358ae45d877d1059aa43dce08eefb39b
Patch0:		%{name}-versions.patch
Patch1:		%{name}-build.patch
URL:		http://apertium.sourceforge.net/
BuildRequires:	apertium-devel >= 3.1
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	lttoolbox-devel >= 3.1
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	apertium >= 3.1
Requires:	libxml2 >= 1:2.6.17
Requires:	lttoolbox >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apertium-based target-language driven HMM-based part-of-speech tagger
trainer.

%description -l pl.UTF-8
Narzędzie Apertium do nauki rozpoznawania części mowy wg języka
docelowego oparte na HMM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	apertium_tagger_training_toolsdir=%{_datadir}/apertium-tagger-training-tools-1.1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	apertium_tagger_training_toolsdir=%{_datadir}/apertium-tagger-training-tools-1.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS README
%attr(755,root,root) %{_bindir}/apertium-SGT
%attr(755,root,root) %{_bindir}/apertium-tagger-apply-rules
%attr(755,root,root) %{_bindir}/apertium-tagger-baum-welch
%attr(755,root,root) %{_bindir}/apertium-tagger-check-parameters
%attr(755,root,root) %{_bindir}/apertium-tagger-eval
%attr(755,root,root) %{_bindir}/apertium-tagger-gen-crp-file
%attr(755,root,root) %{_bindir}/apertium-tagger-gen-dic-file
%attr(755,root,root) %{_bindir}/apertium-tagger-gen-tsx-file
%attr(755,root,root) %{_bindir}/apertium-tagger-prob2txt
%attr(755,root,root) %{_bindir}/apertium-tagger-readwords
%attr(755,root,root) %{_bindir}/apertium-tagger-states-merging
%attr(755,root,root) %{_bindir}/apertium-tagger-supervised
%attr(755,root,root) %{_bindir}/apertium-tagger-tagset-clustering
%attr(755,root,root) %{_bindir}/apertium-tagger-tl-trainer
%attr(755,root,root) %{_bindir}/apertium-trigrams-langmodel
%attr(755,root,root) %{_bindir}/apertium-trigrams-langmodel-perline
%attr(755,root,root) %{_bindir}/apertium-xtract-regex-trules
%{_datadir}/apertium-tagger-training-tools-1.1
%{_pkgconfigdir}/apertium-tagger-training-tools-1.1.pc
