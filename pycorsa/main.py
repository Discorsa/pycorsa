import ac; import acsys
import typing; from typing import Optional, Literal, Callable, TypedDict, Dict
import threading; import logging

class a_3D_object():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
class a_4D_object(a_3D_object):
    def __init__(self, x, y, z, w) -> None:
        super().__init__(x, y, z)
        self.w = w
    
    def as_tire(self):
        self.FL = self.x
        self.FR = self.y
        self.RL = self.z
        self.RR = self.w
        return self

class car():
    """
    This is basically just wrapping everything that uses CAR_ID in parameter in the original python doc
    """
    def __init__(self, car_id: int) -> None:
        self.car_id = car_id
        self.state = self.state(self.car_id)

    class state():
        def __init__(self, car_id) -> None:
            self.car_id = car_id

        def _getCarState(self, info_identifier: Literal[
            'SpeedMS', 'SpeedMPH', 'SpeedKMH', 'Gas', 'Brake', 'Clutch', 'Gear',
            'BestLap', 'CGHeight', 'DriftBestLap', 'DriftLastLap', 'DriftPoints',
            'DriveTrainSpeed', 'RPM', 'InstantDrift', 'IsDriftInvalid', 'IsEngineLimiterOn',
            'LapCount', 'LapInvalidated', 'LapTime', 'LastFF', 'LastLap', 'PerformanceMeter',
            'NormalizedSplinePosition', 'Steer', 'TurboBoost', 'Caster',
            # 3D Vector identifiers
            'AccG', 'LocalAngularVelocity', 'LocalVelocity', 'SpeedTotal', 'Velocity',
            'WheelAngularSpeed', 'WorldPosition',
            # 4D Vector identifiers
            'CamberRad', 'CamberDeg', 'SlipAngle', 'SlipRatio', 'Mz', 'Load', 'TyreRadius',
            'NdSlip', 'TyreSlip', 'Dy', 'CurrentTyresCoreTemp', 'ThermalState',
            'DynamicPressure', 'TyreLoadedRadius', 'SuspensionTravel', 'TyreDirtyLevel',
            # Needs the optional identifier for tyres
            'TyreContactNormal', 'TyreContactPoint', 'TyreHeadingVector', 'TyreRightVector',
            # Needs the optional identified for index O
            'Aero',
        ], optional_identifier: Literal['FL', 'FR', 'RL', 'RR']=None):
            return ac.getCarState(self.car_id, info_identifier, optional_identifier)

        @property
        # TODO: needs to be fixed
        def speed(self) -> Dict[Literal['ms', 'mph', 'kmh'], int]:
            val = {'ms': self.speed_total.z,
                   'mph': self.speed_total.y,
                   'kmh': self.speed_total.x}
            return val
        
        @property
        def gas(self):
            val = self._getCarState('Gas')
            return val
        
        @property
        def brake(self):
            val = self._getCarState('Brake')
            return val
        
        @property
        def clutch(self):
            val = self._getCarState('Clutch')
            return val
        
        @property
        def gear(self):
            val = self._getCarState('Gear')
            return val
        
        @property
        def best_lap(self):
            val = self._getCarState('BestLap')
            return val
        
        @property
        def cgheight(self):
            val = self._getCarState('CGHeight')
            return val
        
        @property
        def best_drift_lap(self):
            val = self._getCarState('DriftBestLap')
            return val
        
        @property
        def last_drift_lap(self):
            val = self._getCarState('DriftLastLap')
            return val
        
        @property
        def drift_points(self):
            val = self._getCarState('DriftPoints')
            return val
        
        @property
        def drive_train_speed(self):
            val = self._getCarState('DriveTrainSpeed')
            return val
        
        @property
        def rpm(self):
            val = self._getCarState('RPM')
            return val
        
        @property
        def instant_drift(self):
            val = self._getCarState('InstantDrift')
            return val
        
        @property
        def drift_invalidated(self):
            val = self._getCarState('IsDriftInvalid')
            return val
        
        @property
        def engine_limiter(self) -> bool:
            val = self._getCarState('IsEngineLimiterOn')
            return bool(val)
        
        @property
        def lap_count(self):
            val = self._getCarState('LapCount')
            return val
        
        @property
        def lap_invalidated(self):
            val = self._getCarState('LapInvalidated')
            return val
        
        @property
        def lap_time(self):
            val = self._getCarState('LapTime')
            return val
        
        @property
        def last_ff(self):
            val = self._getCarState('LastFF')
            return val
        @property
        def last_force_feedback(self):
            return self.last_ff
        
        @property
        def last_lap(self):
            val = self._getCarState('LastLap')
            return val
        
        @property
        def performance_meter(self):
            val = self._getCarState('PerformanceMeter')
            return val
        
        @property
        def normalized_spline_position(self):
            val = self._getCarState('NormalizedSplinePosition')
            return val
        
        @property
        def steer(self):
            val = self._getCarState('Steer')
            return val
        
        @property
        def turbo_boot(self):
            val = self._getCarState('TurboBoost')
            return val
        
        @property
        def caster(self):
            val = self._getCarState('Caster')
            return val
        
        @property
        def accg(self):
            _val = self._getCarState('AccG')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val      
        @property
        def gravitational_acceleration(self):
            return self.accg
        
        @property
        def local_angular_velocity(self):
            _val = self._getCarState('LocalAngularVelocity')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val
                
        @property
        def local_velocity(self):
            _val = self._getCarState('LocalVelocity')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val
                        
        @property
        def speed_total(self):
            _val = self._getCarState('SpeedTotal')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val

        @property
        def velocity(self):
            _val = self._getCarState('Velocity')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val

        @property
        def wheel_angular_speed(self):
            _val = self._getCarState('WheelAngularSpeed')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val
        @property
        def angular_wheel_speed(self):
            return self.wheel_angular_speed

        @property
        def world_position(self):
            _val = self._getCarState('WorldPosition')
            val = a_3D_object(x=_val[0], y=_val[1], z=_val[2])
            return val

        """
        Some 4D objects are related to each tire. So in these cases:  X, Y, Z, W  correspond to  FL, FR, RL, RR  respectively
        """

        @property
        def camber_rad(self):
            _val = self._getCarState('CamberRad')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val

        @property
        def camber_deg(self):
            _val = self._getCarState('CamberDeg')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def slip_angle(self):
            # TODO: check whether this is for tire or not
            _val = self._getCarState('SlipAngle')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3])
            return val

        @property
        def slip_ratio(self):
            _val = self._getCarState('SlipRatio')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def mz(self):
            _val = self._getCarState('Mz')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3])
            return val
        
        @property
        def load(self):
            _val = self._getCarState('Load')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val

        @property
        def tyre_radius(self):
            _val = self._getCarState('TyreRadius')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def nd_slip(self):
            _val = self._getCarState('NdSlip')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3])
            return val
        
        @property
        def tyre_slip(self):
            _val = self._getCarState('TyreSlip')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3])
            return val
        
        @property
        def dy(self):
            _val = self._getCarState('Dy')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3])
            return val
        
        @property
        def current_tyres_core_temp(self):
            _val = self._getCarState('CurrentTyresCoreTemp')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def thermal_state(self):
            _val = self._getCarState('ThermalState')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def dynamic_pressure(self):
            _val = self._getCarState('DynamicPressure')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def tyre_loaded_radius(self):
            _val = self._getCarState('TyreLoadedRadius')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def suspension_travel(self):
            _val = self._getCarState('SuspensionTravel')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def tyre_dirty_level(self):
            _val = self._getCarState('TyreDirtyLevel')
            val = a_4D_object(x=_val[0], y=_val[1], z=_val[2], w=_val[3]).as_tire()
            return val
        
        @property
        def tyre_contact_normal(self):
            responses = dict()
            for direction in ['FL', 'FR', 'RL', 'RR']:
                __val = self._getCarState('TyreContactNormal', direction)
                responses[direction] = __val
            _val = a_4D_object(x=responses['FL'], y=responses['FR'], z=responses['RL'], w=responses['RR']).as_tire()
            return _val
        
        @property
        def tyre_contact_point(self):
            responses = dict()
            for direction in ['FL', 'FR', 'RL', 'RR']:
                __val = self._getCarState('TyreContactPoint', direction)
                responses[direction] = __val
            _val = a_4D_object(x=responses['FL'], y=responses['FR'], z=responses['RL'], w=responses['RR']).as_tire()
            return _val
        
        @property
        def tyre_heading_vector(self):
            responses = dict()
            for direction in ['FL', 'FR', 'RL', 'RR']:
                __val = self._getCarState('TyreHeadingVector', direction)
                responses[direction] = __val
            _val = a_4D_object(x=responses['FL'], y=responses['FR'], z=responses['RL'], w=responses['RR']).as_tire()
            return _val
        
        @property
        def tyre_right_vector(self):
            responses = dict()
            for direction in ['FL', 'FR', 'RL', 'RR']:
                __val = self._getCarState('TyreRightVector', direction)
                responses[direction] = __val
            _val = a_4D_object(x=responses['FL'], y=responses['FR'], z=responses['RL'], w=responses['RR']).as_tire()
            return _val
        

    def _getDriverName(self):
        val = ac._getDriverName(self.car_id)
        if isinstance(val, str):
            return val
        if val == -1:
            return None
    @property
    def driver_name(self):
        self.getDriverName()

    def _getTrackName(self):
        val = ac.getTrackName(self.car_id)
        if isinstance(val, str):
            return val
        if val == -1:
            return None
    @property
    def track(self):
        return self._getTrackName()
    
    def _getTrackConfiguration(self):
        val = ac.getTrackConfiguration(self.car_id)
        if isinstance(val, str):
            return val
        if val == -1:
            return None
    @property
    def track_configuration(self):
        return self._getTrackConfiguration()
    
    def _getCarName(self):
        val = ac.getCarName(self.car_id)
        if isinstance(val, str):
            return val
        if val == -1:
            return None
    @property
    def car_name(self):
        return self._getCarName()
    
    def _getLastSplits(self):
        val = ac.getLastSplits(self.car_id)
        if isinstance(val, list):
            return val
        if val == -1:
            return None
    @property
    def last_splits(self):
        return self._getLastSplits()
    @property
    def last_sectors(self):
        return self._getLastSplits()
    
    def _isCarInPitline(self):
        val = ac.isCarInPitline(self.car_id)
        if val ==  1:
            return True
        if not val == 1:
            return False
    @property
    def is_in_pitline(self):
        return self._isCarInPitline()
    
    def _isCarInPit(self):
        val = ac.isCarInPit(self.car_id)
        if val == 1:
            return True
        if not val == 1:
            return False
    @property
    def is_in_pit(self):
        return self._isCarInPit()
    
    def _isConnected(self):
        val = ac.isConnected(self.car_id)
        if val == 1:
            return True
        if not val == 1:
            return False
    @property
    def is_connected(self):
        return self._isConnected()
    
    def _getCarBallast(self):
        val = ac.getCarBallast(self.car_id)
        return val
    @property
    def ballast(self):
        return self._getCarBallast
    
    def _getCarMinHeight(self):
        val = ac.getCarMinHeight(self.car_id)
        return val
    @property
    def min_height(self):
        return self._getCarMinHeight

    def _getCarLeaderboardPosition(self):
        val = ac.getCarLeaderboardPosition(self.car_id)
        return val
    @property
    def leaderboard_position(self):
        return self._getCarLeaderboardPosition()
    
    def _getCarRealTimeLeaderboardPosition(self):
        val = ac.getCarRealTimeLeaderboardPosition(self.car_id)
        return val
    @property
    def realtime_leaderboard_position(self):
        return self._getCarRealTimeLeaderboardPosition()
    
    def _getCarFFB(self):
        if not self.car_id == 0:
            raise Exception('Fetching car FFB is only allowed for the current players car (id should be 0)')
        val = ac.getCarFFB(self.car_id)
        return val
    @property
    def ffb_gain(self):
        return self._getCarFFB()
        
    def setCarFFB(self, value_to_add: int):
        if not self.car_id == 0:
            raise Exception('Setting car FFB is only allowed for the current players car (id should be 0)')
        ac.setCarFFB(value_to_add)
        return self.ffb_gain


class window_management():

    class generalAppManagement():
        def __init__(self, control_identifier, position, size) -> None:
            self.control_identifier = control_identifier

            self.position = position
            self.size = size

            self.updatePosition(control_identifier, position[0], position[1])
            self.updateSize(control_identifier, size[0], size[1])
        
        def updatePosition(self, position: list):
            ac.setPosition(self.control_identifier, position[0], position[1])
        
        def updateSize(self, size: list):
            ac.setSize(self.control_identifier, size[0], size[1])


    class acButton(generalAppManagement):
        def __init__(self, appWindow, title: str, position: list, size: list, eventListener: Callable) -> None:
            _button = ac.addButton(appWindow, title)
            self._button = _button
            super().__init__(_button, position, size)

            self.updateOnClickedListener(_button, eventListener)
        
        def updateOnClickedListener(self, eventListener: Callable):
            ac.addOnClickedListener(self.control_identifier, eventListener)

