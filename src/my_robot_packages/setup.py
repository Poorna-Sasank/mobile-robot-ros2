from setuptools import find_packages, setup

package_name = 'my_robot_packages'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='comrade',
    maintainer_email='comrade@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "vel_pub = my_robot_packages.velocity_publisher:main",
            "collision_detector_node = my_robot_packages.collision_detection_algorithm:main"
        ],
    },
)
