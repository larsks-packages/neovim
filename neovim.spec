%global commit 51055c14a623ca824d69b257304f0dd813cfda1f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           neovim
Version:        0.1.2
Release:        77.git%{shortcommit}%{?dist}
Summary:        vim for the 21st century
License:        ASL 2.0
URL:            http://neovim.org/
Source0:        https://github.com/neovim/neovim/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  lua
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  unzip

Provides:       bundled(libuv) = 1.7.3
Provides:       bundled(msgpack-c) = 1.0.0
Provides:       bundled(luajit) = 2.0.4
Provides:       bundled(luarocks) = 5d8a16526573b36d5b22aa74866120c998466697
Provides:       bundled(unibilium) = 1.2.0
Provides:       bundled(libtermkey) = 0.18
Provides:       bundled(libvterm) = 1b745d29d45623aa8d22a7b9288c7b0e331c7088
Provides:       bundled(jemalloc) = 4.0.2

# Bundled licenses:
# libuv:        Node
# msgpack-c:    ASL 2.0
# luajit:       MIT
# luarocks:     MIT
# unibilium:    {L}GPLv3+
# libtermkey:   MIT
# libvterm:     GPLv2
# jemalloc:     BSD

%description
Neovim is a project that seeks to aggressively refactor Vim in order to:
* Simplify maintenance and encourage contributions
* Split the work between multiple developers
* Enable the implementation of new/modern user interfaces without any
  modifications to the core source
* Improve extensibility with a new plugin architecture

%package vim-compat
Requires: %{name} = %{version}
Summary: Compatability symlinks for neovim
Conflicts: vim-enhanced

%description vim-compat
Contains compatability symlinks for people who are used to typing "vim".


%prep
%setup -q -n %{name}-%{commit}


%build
export CC=clang
export CXX=clang++

mkdir -p .deps
cd .deps
cmake -DCMAKE_BUILD_TYPE=RELEASE ../third-party
make
cd ..
make clean
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make
cd ..


%install
DESTDIR=%{buildroot} make install
%find_lang nvim
ln -s nvim %{buildroot}%{_bindir}/vim

%files -f nvim.lang
%doc README.md
%docdir /usr/share/man
%license LICENSE
%{_bindir}/nvim
%{_datadir}/nvim/runtime/*
/usr/share/man

%files vim-compat
%{_bindir}/vim

%changelog
* Wed Dec 09 2015 David Personette <dperson@gmail.com> - 0.1.1-76.git4a1c36e
- snapshot @ 4a1c36e953559382362b79be7630a64163c43ef2

* Sat Nov 21 2015 David Personette <dperson@gmail.com> - 0.1.0-75.git1fbb567
- snapshot @ 1fbb56795d16783f9a97e25e3b71ab3ac2a644dc

* Fri Nov 06 2015 David Personette <dperson@gmail.com> - 0.1.0-74.git9499432
- snapshot @ 9499432d7fb1a96c5faf42c6ce538dbf4f7a9463

* Fri Oct 30 2015 David Personette <dperson@gmail.com> - 0.0.0-73.git4abf108
- snapshot @ 4abf108f4639af1c35bc0554a069d878a50fcea0

* Mon Oct 26 2015 David Personette <dperson@gmail.com> - 0.0.0-72.git29d64a9
- snapshot @ 29d64a901df6eff436b100374b2a240eea1906d9

* Tue Oct 20 2015 David Personette <dperson@gmail.com> - 0.0.0-71.gite38cbb9
- snapshot @ e38cbb93670272d0da15c60222a123b88ec55002
- update versions for libuv, unibilium, libtermkey, and jemalloc
- update build steps, and build requirements

* Wed Aug 12 2015 David Personette <dperson@gmail.com> - 0.0.0-70.gita6c6128
- snapshot @ a6c612868186278ca8428a8dfaa4064954a920c1

* Sun Jul 26 2015 David Personette <dperson@gmail.com> - 0.0.0-69.git7a6bf3f
- snapshot @ 7a6bf3f418c5ad94ac2ac71f21275a87d08e87b9

* Sun Jul 19 2015 David Personette <dperson@gmail.com> - 0.0.0-68.git5fdaac4
- snapshot @ fb0ebb2a3a220a2e744efabed82beb08d88e158d

* Sat Jul 11 2015 David Personette <dperson@gmail.com> - 0.0.0-67.git5fdaac4
- snapshot @ 5fdaac45a60cb555579fd2f10fad7e52c67ae042

* Sun Jul 05 2015 David Personette <dperson@gmail.com> - 0.0.0-66.git5305338
- snapshot @ 53053381674b1cca4c60c3657f31ea05fd935278

* Sun May 31 2015 David Personette <dperson@gmail.com> - 0.0.0-65.git28ad7b5
- snapshot @ 7dc241ac782e3a469d73d5f9a7baeba4e6107333
- update versions for luarocks

* Tue May 26 2015 David Personette <dperson@gmail.com> - 0.0.0-64.git28ad7b5
- snapshot @ 5a9ad68b258f33ebd7fa0a5da47b308f50f1e5e7
- update versions for luajit and unibilium
- add /usr/share/man to spec

* Sun May 17 2015 David Personette <dperson@gmail.com> - 0.0.0-63.git28ad7b5
- snapshot @ d9acfbd471403a4f11ad050665633d3311a462d9
- update version for libuv

* Sun May 03 2015 David Personette <dperson@gmail.com> - 0.0.0-62.git28ad7b5
- snapshot @ 28ad7b5026d731a832bf60ba4c497c9e3d97e9ff

* Sun Apr 26 2015 David Personette <dperson@gmail.com> - 0.0.0-61.git1a636ea
- snapshot @ 1a636eabd555c3631348bae8291dbb7974523310

* Sun Apr 19 2015 David Personette <dperson@gmail.com> - 0.0.0-60.git119a3f2
- snapshot @ 639504894610361198447ddaaa557b4877136682
- Add bundled jemalloc

* Sat Apr 11 2015 David Personette <dperson@gmail.com> - 0.0.0-59.git119a3f2
- snapshot @ e584fe00570a522154ce856581006644e766f88f

* Wed Apr 01 2015 David Personette <dperson@gmail.com> - 0.0.0-58.git119a3f2
- snapshot @ 119a3f2485e057b05ca46fc40e59f1434913d488
- Add bundled libvterm

* Sun Feb 22 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-57.git3e29231
- snapshot @ 3e292316846708dfc1153d55fbd5f012c2da8a35

* Sat Feb 21 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-56.gitc48f835
- snapshot @ c48f835749913f48267ed3b389bdd333e19e6dc4

* Sat Feb 21 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-55.git486d2e9
- snapshot @ 486d2e944dffb30d97d65c88bbcc77f6fd1208f6

* Fri Feb 20 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-54.git03dd211
- snapshot @ 03dd2114a78f513c362ccc5ec4de700f11a2db0e

* Thu Feb 19 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-53.gitb1d079c
- snapshot @ b1d079c83b3dd459114d1ba7c2ff1b07a9ee3e9e

* Wed Feb 18 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-52.git366662d
- snapshot @ 366662d932551e558d10f09887ddf144ed5db34b
- Add git tarball generator script.

* Tue Feb 17 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-51.gitfd636fc
- snapshot @ 66a03a7385dfd11503d22d8cc9dc6a972e27dcc2

* Mon Feb 16 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-50.gitfd636fc
- snapshot @ fd636fc6dcd8a547daab1544432877bf8efa0c1e

* Sun Feb 15 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-49.git6e99287
- snapshot @ 6e992876ea043fe7fe748d5da5e3b511b60d06a5

* Thu Feb 12 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-48.gitec2c299
- snapshot @ ec2c2994e6e5ca79ed21d0c6d7176c2f065a17cc

* Wed Feb 11 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-47.git5976251
- snapshot @ 5976251bb91a7d3967cf268f0eeed1f5d756ba7a

* Tue Feb 10 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-46.gitec5e945
- snapshot @ ec5e94518e8e631e4deced07cb5127d305b24d27
- Update rev of bundled msgpack-c (https://github.com/neovim/neovim/pull/1900)

* Mon Feb 09 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-45.gitb0fb7ea
- snapshot @ b0fb7ea19d4f102bd86c34cfa2ac62754712bd0a
- Build with clang.

* Sat Feb 07 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-44.git28dcfcf
- snapshot @ 28dcfcf325d222ae311bf972997c92bc1efd3e8f

* Wed Feb 04 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-43.git7751cd2
- Use license macro

* Tue Feb 03 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-42.git7751cd2
- snapshot @ 7751cd21f5ae8952f578a0ccd892e32c95a4ae8a

* Sat Jan 31 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-41.git6196cab
- snapshot @ 6196cab139b52cd412c198f38626ec7f7688995e

* Fri Jan 30 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-40.git41fe3cb
- snapshot @ 41fe3cb196b78d6570555c4f21b04969357a4199

* Thu Jan 29 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-39.git9023f62
- snapshot @ 9023f62707c47cd0dc9bbd711099faee0d93e3a6

* Tue Jan 27 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-38.git6bc8c7b
- snapshot @ 6bc8c7be3a808f66d2c47bfe463a1346490da7f4

* Mon Jan 26 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-37.gitd304642
- snapshot @ d30464264af2b5aa261281e221d936095dbab864

* Sat Jan 24 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-36.git65adcc2
- snapshot @ 65adcc269971b55418769a8eca8e49f3e0191e14

* Fri Jan 23 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-35.git641df7b
- snapshot @ 641df7be9cc8168399ea05d61f7009770880f28f

* Wed Jan 21 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-34.gitc3028e4
- snapshot @ c3028e435392a7b647f79be826c054ef76b0d577

* Mon Jan 19 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-33.git617c00b
- snapshot @ 617c00bd49c2bdb05c8ef31f94e206ba3f80f694

* Sun Jan 18 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-32.gitc7f4e55
- snapshot @ c7f4e553629f9ac667dee1e920b96c7c327380f6
- ^ Excuse to push a build through rawhide on copr.

* Sat Jan 17 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-31.gitbff48b2
- snapshot at bff48b23d700d6202e1c85564cd7fcb1b3ce4c34
- Add provides for bundled libs
- Add bundled licenses note

* Thu Jan 15 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-30.gita99d33a
- snapshot @ 5c6348e9995b0dde23a2de99263e9e0e3a72fcd2

* Tue Jan 13 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-29.gita99d33a
- snapshot @ a99d33ad9a6a81400a04712f769180ef700787b4

* Sat Jan 10 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-28.gita684cc1
- snapshot @ a684cc175a6c1ca2cfc3bff2d68383d32008cb3b

* Fri Jan 09 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-27.gitb16162b
- snapshot @ 515acf72247518ed34c5f76ce6fe007217cd94bb

* Fri Jan 09 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-26.gitb16162b
- snapshot @ b16162b00fa78ab2f3ef8a114d409213efcb578b

* Fri Jan 02 2015 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-25.git91b378d
- snapshot @ 91b378d349425d0ad435c06fc341de5aa2f7b5c9

* Wed Dec 31 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-24.gita31bcfb
- Misc:
- Clean-up, tidy-up, extra pick-ups from auto-br-rpmbuild

* Tue Dec 30 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-23.gita31bcfb
- Add git build dep, mock build.
- Drop specified no. of jobs for ninja.

* Tue Dec 30 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-22.gita31bcfb
- snapshot @ a31bcfb98afbe4d845911b4d90255c18769f197a

* Mon Dec 29 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-21.gitb229908
- snapshot @ b229908587928249f7ecc787615470c235dbfaf4

* Sat Dec 27 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-20.git4ff4b93
- snapshot @ 4ff4b9306d9ccd26c6e7c8e9b663788aa53d84ec

* Fri Dec 26 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-19.git7231a23
- Cleanups.

* Thu Dec 25 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-18.git7231a23
- snapshot @ 7231a23cf651f8d950f53d4537e650085a41fb66

* Wed Dec 24 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-17.git5998552
- snapshot @ 59985523b851fe61b62afcef69f4564f064cbc0a

* Tue Dec 23 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-16.gitc3de63b
- snapshot @ c3de63bfbc168cd8ccc53dbb3e587043c11f7276

* Sat Dec 20 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-15.git5fe519f
- snapshot @ 5fe519f78a790abbd15d24f05ce19bed22b07990

* Thu Dec 18 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-14.git1eef530
- snapshot @ 1eef5303514a8499fd376270bd89a40e2d3eafbb
- Adapt to upstream build changes

* Tue Dec 16 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-13.git3a61b84
- snapshot @ 3a61b84543c7cd843fe60d9ec4b356fb18f6a726

* Mon Dec 15 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-12.gitc63b736
- snapshot @ c63b736921d143354e3a7a607deafdb72c0ae8f9
- Back tp previous naming scheme, dnf changes caught me off-guard.

* Sun Dec 14 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0_20141213-1.git677a3f4
- snapshot @ 677a3f42c0f0821ddeed34728c8708fa4d0742cc
- Try better versioning.

* Wed Dec 10 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-11.git951d00
- snapshot @ 951d00a492c58449d3c241fa710a83051f45dcb7

* Sun Dec 07 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-10.gitc5b9e5
- snapshot @ c5b9e5d1d317b74d4adf7637cd9081be4ee52722
- bdep on libtool for libunibilium

* Sun Dec 07 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-9.gitfa9d44
- snapshot @ fa9d44374b84e6768142e8d3751fe215c14796c7

* Thu Dec 04 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-8.git81530e
- snapshot @ 81530e581615528bc4f57348ed92c46ca49a4657
- Bundled libuv now at 1.0.1, we can drop the dtrace patch.

* Wed Dec 03 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-7.gitcb86eca
- snapshot @ cb86eca91f9bdffe8b0214664169093d41902415

* Tue Dec 02 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-6.git8885118
- snapshot @ 888511862bc7b0850e2695e3edd46212dc78cc47

* Fri Nov 28 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-5.gitad848ce
- snapshot @ 3bbbeaf2c9658222f31c29bc0ab27b9f125fb27c

* Tue Nov 25 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-4.git3bbbeaf
- snapshot @ 3bbbeaf2c9658222f31c29bc0ab27b9f125fb27c

* Sun Nov 23 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-3.git4b89903
- snapshot @ 4b89903a22894c8f0847ed6c206f2dfcae60b4d1

* Thu Nov 20 2014 Ray Griffin <rorgoroth@openmailbox.org> - 0.0.0-2.git32ec851
- Update to newer snapshot
- Use bundled libs since some dont exist or are stable version
- Patch to fix libuv dtrace build error
- Use ninja as the builder
- Install runtime

* Wed Jul  9 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-1.git308953e
- Initial package
