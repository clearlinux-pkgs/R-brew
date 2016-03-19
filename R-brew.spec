#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-brew
Version  : 1.0
Release  : 17
URL      : http://cran.r-project.org/src/contrib/brew_1.0-6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/brew_1.0-6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n brew

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library brew
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library brew


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/brew/DESCRIPTION
/usr/lib64/R/library/brew/INDEX
/usr/lib64/R/library/brew/Meta/Rd.rds
/usr/lib64/R/library/brew/Meta/hsearch.rds
/usr/lib64/R/library/brew/Meta/links.rds
/usr/lib64/R/library/brew/Meta/nsInfo.rds
/usr/lib64/R/library/brew/Meta/package.rds
/usr/lib64/R/library/brew/NAMESPACE
/usr/lib64/R/library/brew/R/brew
/usr/lib64/R/library/brew/R/brew.rdb
/usr/lib64/R/library/brew/R/brew.rdx
/usr/lib64/R/library/brew/Sweave-test-1-006.eps
/usr/lib64/R/library/brew/Sweave-test-1-006.pdf
/usr/lib64/R/library/brew/Sweave-test-1-007.eps
/usr/lib64/R/library/brew/Sweave-test-1-007.pdf
/usr/lib64/R/library/brew/Sweave-test-1.aux
/usr/lib64/R/library/brew/Sweave-test-1.dvi
/usr/lib64/R/library/brew/Sweave-test-1.log
/usr/lib64/R/library/brew/Sweave-test-1.orig.dvi
/usr/lib64/R/library/brew/Sweave-test-1.tex
/usr/lib64/R/library/brew/brew-test-1-1.eps
/usr/lib64/R/library/brew/brew-test-1-1.pdf
/usr/lib64/R/library/brew/brew-test-1-2.eps
/usr/lib64/R/library/brew/brew-test-1.aux
/usr/lib64/R/library/brew/brew-test-1.brew
/usr/lib64/R/library/brew/brew-test-1.dvi
/usr/lib64/R/library/brew/brew-test-1.log
/usr/lib64/R/library/brew/brew-test-1.tex
/usr/lib64/R/library/brew/brew-test-2-table.brew
/usr/lib64/R/library/brew/brew-test-2.aux
/usr/lib64/R/library/brew/brew-test-2.brew
/usr/lib64/R/library/brew/brew-test-2.dvi
/usr/lib64/R/library/brew/brew-test-2.html
/usr/lib64/R/library/brew/brew-test-2.log
/usr/lib64/R/library/brew/brew-test-2.tex
/usr/lib64/R/library/brew/brew-test-3.brew
/usr/lib64/R/library/brew/broken.brew
/usr/lib64/R/library/brew/catprint.brew
/usr/lib64/R/library/brew/example1.brew
/usr/lib64/R/library/brew/example2.brew
/usr/lib64/R/library/brew/featurefull.brew
/usr/lib64/R/library/brew/help/AnIndex
/usr/lib64/R/library/brew/help/aliases.rds
/usr/lib64/R/library/brew/help/brew.rdb
/usr/lib64/R/library/brew/help/brew.rdx
/usr/lib64/R/library/brew/help/paths.rds
/usr/lib64/R/library/brew/html/00Index.html
/usr/lib64/R/library/brew/html/R.css
