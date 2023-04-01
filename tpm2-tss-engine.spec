Summary:	TPM2 TSS engine for OpenSSL
Summary(pl.UTF-8):	Silnik TPM2 TSS dla OpenSSL-a
Name:		tpm2-tss-engine
Version:	1.2.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/tpm2-software/tpm2-tss-engine/releases
Source0:	https://github.com/tpm2-software/tpm2-tss-engine/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d66cb44c77ed537beaab53e5b72cf273
URL:		https://github.com/tpm2-software/tpm2-tss-engine
# for tests
#BuildRequires:	cmocka-devel >= 1.0
#BuildRequires:	expect
BuildRequires:	openssl-devel >= 1.0.2g
BuildRequires:	pandoc
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	tpm2-tss-devel >= 2.4
Requires:	openssl-engine-tpm2-tss = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		enginesdir	%(pkg-config --variable=enginesdir libcrypto)

%description
The tpm2-tss-engine project implements a cryptographic engine for
OpenSSL for TPM 2.0 (Trusted Platform Module 2.0) using the tpm2-tss
software stack that follows the TCG (Trusted Computing Group) TSS 2.0
(TPM Software Stack 2.0). It uses the ESAPI (Enhanced System API)
interface of the TSS 2.0 for downwards communication. It supports RSA
decryption and signatures as well as ECDSA signatures.

%description -l pl.UTF-8
Projekt tpm2-tss-engine implementuje silnik kryptograficzny OpenSSL
dla TPM 2.0 (Trusted Platform Module 2.0), wykorzystujący stos
programowy tpm2-tss, zgodny ze specyfikacją TCG (Trusted Computing
Group) TSS 2.0 (TPM Software Stack 2.0). Wykorzystuje interfejs ESAPI
(Enhanced System API) TSS 2.0 do komunikacji. Obsługuje
odszyfrowywanie i podpisy RSA oraz podpisy ECDSA.
 
%package -n bash-completion-tpm2-tss-engine
Summary:	Bash completion for tpm2tss-genkey program
Summary(pl.UTF-8):	Bashowe dopełnianie argumentów programu tpm2tss-genkey
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-tpm2-tss-engine
Bash completion for tpm2tss-genkey program.

%description -n bash-completion-tpm2-tss-engine -l pl.UTF-8
Bashowe dopełnianie argumentów programu tpm2tss-genkey.

%package -n openssl-engine-tpm2-tss
Summary:	TPM2 TSS engine for OpenSSL
Summary(pl.UTF-8):	Silnik TPM2 TSS dla OpenSSL-a
Group:		Libraries
Requires:	openssl >= 1.0.2g

%description -n openssl-engine-tpm2-tss
The tpm2-tss-engine project implements a cryptographic engine for
OpenSSL for TPM 2.0 (Trusted Platform Module 2.0) using the tpm2-tss
software stack that follows the TCG (Trusted Computing Group) TSS 2.0
(TPM Software Stack 2.0). It uses the ESAPI (Enhanced System API)
interface of the TSS 2.0 for downwards communication. It supports RSA
decryption and signatures as well as ECDSA signatures.

%description -n openssl-engine-tpm2-tss -l pl.UTF-8
Projekt tpm2-tss-engine implementuje silnik kryptograficzny OpenSSL
dla TPM 2.0 (Trusted Platform Module 2.0), wykorzystujący stos
programowy tpm2-tss, zgodny ze specyfikacją TCG (Trusted Computing
Group) TSS 2.0 (TPM Software Stack 2.0). Wykorzystuje interfejs ESAPI
(Enhanced System API) TSS 2.0 do komunikacji. Obsługuje
odszyfrowywanie i podpisy RSA oraz podpisy ECDSA.

%package devel
Summary:	Header file for TPM2-TSS OpenSSL engine functions
Summary(pl.UTF-8):	Plik nagłówkowy funkcji silnika OpenSSL TPM2-TSS
Group:		Development/Libraries
Requires:	openssl-engine-tpm2-tss = %{version}-%{release}
BuildArch:	noarch

%description devel
Header file for TPM2-TSS OpenSSL engine functions.

%description devel -l pl.UTF-8
Plik nagłówkowy funkcji silnika OpenSSL TPM2-TSS.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-completionsdir=%{bash_compdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{enginesdir}/libtpm2tss.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tpm2tss-genkey
%{_mandir}/man1/tpm2tss-genkey.1*

%files -n bash-completion-tpm2-tss-engine
%defattr(644,root,root,755)
%{bash_compdir}/tpm2tss-genkey

%files -n openssl-engine-tpm2-tss
%doc AUTHORS CHANGELOG.md LICENSE README.md
%defattr(644,root,root,755)
%attr(755,root,root) %{enginesdir}/libtpm2tss.so
%attr(755,root,root) %{enginesdir}/tpm2tss.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/tpm2-tss-engine.h
%{_mandir}/man3/tpm2tss_*.3*
