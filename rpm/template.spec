Name:           ros-jade-gazebo-ros
Version:        2.5.1
Release:        2%{?dist}
Summary:        ROS gazebo_ros package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-gazebo-msgs
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-generation
Requires:       ros-jade-roscpp
Requires:       ros-jade-rosgraph-msgs
Requires:       ros-jade-roslib
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf
Requires:       tinyxml-devel
BuildRequires:  gazebo-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-gazebo-msgs
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rosgraph-msgs
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf
BuildRequires:  tinyxml-devel

%description
Provides ROS plugins that offer message and service publishers for interfacing
with Gazebo through ROS. Formally simulator_gazebo/gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Aug 17 2015 John Hsu <hsu@osrfoundation.org> - 2.5.1-2
- Autogenerated by Bloom

* Sun Aug 16 2015 John Hsu <hsu@osrfoundation.org> - 2.5.1-1
- Autogenerated by Bloom

* Sun Aug 16 2015 John Hsu <hsu@osrfoundation.org> - 2.5.1-0
- Autogenerated by Bloom

* Wed Aug 12 2015 John Hsu <hsu@osrfoundation.org> - 2.5.0-1
- Autogenerated by Bloom

