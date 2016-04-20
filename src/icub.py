# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_icub', [dirname(__file__)])
        except ImportError:
            import _icub
            return _icub
        if fp is not None:
            try:
                _mod = imp.load_module('_icub', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _icub = swig_import_helper()
    del swig_import_helper
else:
    import _icub
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _icub.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _icub.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _icub.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _icub.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _icub.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _icub.SwigPyIterator_equal(self, x)

    def copy(self):
        return _icub.SwigPyIterator_copy(self)

    def next(self):
        return _icub.SwigPyIterator_next(self)

    def __next__(self):
        return _icub.SwigPyIterator___next__(self)

    def previous(self):
        return _icub.SwigPyIterator_previous(self)

    def advance(self, n):
        return _icub.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _icub.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _icub.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _icub.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _icub.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _icub.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _icub.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _icub.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import yarp
class CartesianEventHandler(yarp.BufferedPortBottle):
    """Proxy of C++ CartesianEventHandler class."""

    __swig_setmethods__ = {}
    for _s in [yarp.BufferedPortBottle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CartesianEventHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [yarp.BufferedPortBottle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CartesianEventHandler, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def setInterface(self, interface):
        """setInterface(CartesianEventHandler self, ClientCartesianController interface)"""
        return _icub.CartesianEventHandler_setInterface(self, interface)

    __swig_destroy__ = _icub.delete_CartesianEventHandler
    __del__ = lambda self: None
CartesianEventHandler_swigregister = _icub.CartesianEventHandler_swigregister
CartesianEventHandler_swigregister(CartesianEventHandler)

class ClientCartesianController(yarp.DeviceDriver, yarp.ICartesianControl):
    """Proxy of C++ ClientCartesianController class."""

    __swig_setmethods__ = {}
    for _s in [yarp.DeviceDriver, yarp.ICartesianControl]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ClientCartesianController, name, value)
    __swig_getmethods__ = {}
    for _s in [yarp.DeviceDriver, yarp.ICartesianControl]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ClientCartesianController, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(ClientCartesianController self) -> ClientCartesianController
        __init__(ClientCartesianController self, Searchable config) -> ClientCartesianController
        """
        this = _icub.new_ClientCartesianController(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def open(self, config):
        """open(ClientCartesianController self, Searchable config) -> bool"""
        return _icub.ClientCartesianController_open(self, config)


    def close(self):
        """close(ClientCartesianController self) -> bool"""
        return _icub.ClientCartesianController_close(self)


    def setTrackingMode(self, f):
        """setTrackingMode(ClientCartesianController self, bool const f) -> bool"""
        return _icub.ClientCartesianController_setTrackingMode(self, f)


    def getTrackingMode(self, f):
        """getTrackingMode(ClientCartesianController self, bool * f) -> bool"""
        return _icub.ClientCartesianController_getTrackingMode(self, f)


    def setReferenceMode(self, f):
        """setReferenceMode(ClientCartesianController self, bool const f) -> bool"""
        return _icub.ClientCartesianController_setReferenceMode(self, f)


    def getReferenceMode(self, f):
        """getReferenceMode(ClientCartesianController self, bool * f) -> bool"""
        return _icub.ClientCartesianController_getReferenceMode(self, f)


    def setPosePriority(self, p):
        """setPosePriority(ClientCartesianController self, yarp::os::ConstString const & p) -> bool"""
        return _icub.ClientCartesianController_setPosePriority(self, p)


    def getPosePriority(self, p):
        """getPosePriority(ClientCartesianController self, yarp::os::ConstString & p) -> bool"""
        return _icub.ClientCartesianController_getPosePriority(self, p)


    def getPose(self, *args):
        """
        getPose(ClientCartesianController self, Vector x, Vector o, Stamp stamp=None) -> bool
        getPose(ClientCartesianController self, Vector x, Vector o) -> bool
        getPose(ClientCartesianController self, int const axis, Vector x, Vector o, Stamp stamp=None) -> bool
        getPose(ClientCartesianController self, int const axis, Vector x, Vector o) -> bool
        """
        return _icub.ClientCartesianController_getPose(self, *args)


    def goToPose(self, xd, od, t=0.0):
        """
        goToPose(ClientCartesianController self, Vector xd, Vector od, double const t=0.0) -> bool
        goToPose(ClientCartesianController self, Vector xd, Vector od) -> bool
        """
        return _icub.ClientCartesianController_goToPose(self, xd, od, t)


    def goToPosition(self, xd, t=0.0):
        """
        goToPosition(ClientCartesianController self, Vector xd, double const t=0.0) -> bool
        goToPosition(ClientCartesianController self, Vector xd) -> bool
        """
        return _icub.ClientCartesianController_goToPosition(self, xd, t)


    def goToPoseSync(self, xd, od, t=0.0):
        """
        goToPoseSync(ClientCartesianController self, Vector xd, Vector od, double const t=0.0) -> bool
        goToPoseSync(ClientCartesianController self, Vector xd, Vector od) -> bool
        """
        return _icub.ClientCartesianController_goToPoseSync(self, xd, od, t)


    def goToPositionSync(self, xd, t=0.0):
        """
        goToPositionSync(ClientCartesianController self, Vector xd, double const t=0.0) -> bool
        goToPositionSync(ClientCartesianController self, Vector xd) -> bool
        """
        return _icub.ClientCartesianController_goToPositionSync(self, xd, t)


    def getDesired(self, xdhat, odhat, qdhat):
        """getDesired(ClientCartesianController self, Vector xdhat, Vector odhat, Vector qdhat) -> bool"""
        return _icub.ClientCartesianController_getDesired(self, xdhat, odhat, qdhat)


    def askForPose(self, *args):
        """
        askForPose(ClientCartesianController self, Vector xd, Vector od, Vector xdhat, Vector odhat, Vector qdhat) -> bool
        askForPose(ClientCartesianController self, Vector q0, Vector xd, Vector od, Vector xdhat, Vector odhat, Vector qdhat) -> bool
        """
        return _icub.ClientCartesianController_askForPose(self, *args)


    def askForPosition(self, *args):
        """
        askForPosition(ClientCartesianController self, Vector xd, Vector xdhat, Vector odhat, Vector qdhat) -> bool
        askForPosition(ClientCartesianController self, Vector q0, Vector xd, Vector xdhat, Vector odhat, Vector qdhat) -> bool
        """
        return _icub.ClientCartesianController_askForPosition(self, *args)


    def getDOF(self, curDof):
        """getDOF(ClientCartesianController self, Vector curDof) -> bool"""
        return _icub.ClientCartesianController_getDOF(self, curDof)


    def setDOF(self, newDof, curDof):
        """setDOF(ClientCartesianController self, Vector newDof, Vector curDof) -> bool"""
        return _icub.ClientCartesianController_setDOF(self, newDof, curDof)


    def getRestPos(self, curRestPos):
        """getRestPos(ClientCartesianController self, Vector curRestPos) -> bool"""
        return _icub.ClientCartesianController_getRestPos(self, curRestPos)


    def setRestPos(self, newRestPos, curRestPos):
        """setRestPos(ClientCartesianController self, Vector newRestPos, Vector curRestPos) -> bool"""
        return _icub.ClientCartesianController_setRestPos(self, newRestPos, curRestPos)


    def getRestWeights(self, curRestWeights):
        """getRestWeights(ClientCartesianController self, Vector curRestWeights) -> bool"""
        return _icub.ClientCartesianController_getRestWeights(self, curRestWeights)


    def setRestWeights(self, newRestWeights, curRestWeights):
        """setRestWeights(ClientCartesianController self, Vector newRestWeights, Vector curRestWeights) -> bool"""
        return _icub.ClientCartesianController_setRestWeights(self, newRestWeights, curRestWeights)


    def getLimits(self, axis, min, max):
        """getLimits(ClientCartesianController self, int const axis, double * min, double * max) -> bool"""
        return _icub.ClientCartesianController_getLimits(self, axis, min, max)


    def setLimits(self, axis, min, max):
        """setLimits(ClientCartesianController self, int const axis, double const min, double const max) -> bool"""
        return _icub.ClientCartesianController_setLimits(self, axis, min, max)


    def getTrajTime(self, t):
        """getTrajTime(ClientCartesianController self, double * t) -> bool"""
        return _icub.ClientCartesianController_getTrajTime(self, t)


    def setTrajTime(self, t):
        """setTrajTime(ClientCartesianController self, double const t) -> bool"""
        return _icub.ClientCartesianController_setTrajTime(self, t)


    def getInTargetTol(self, tol):
        """getInTargetTol(ClientCartesianController self, double * tol) -> bool"""
        return _icub.ClientCartesianController_getInTargetTol(self, tol)


    def setInTargetTol(self, tol):
        """setInTargetTol(ClientCartesianController self, double const tol) -> bool"""
        return _icub.ClientCartesianController_setInTargetTol(self, tol)


    def getJointsVelocities(self, qdot):
        """getJointsVelocities(ClientCartesianController self, Vector qdot) -> bool"""
        return _icub.ClientCartesianController_getJointsVelocities(self, qdot)


    def getTaskVelocities(self, xdot, odot):
        """getTaskVelocities(ClientCartesianController self, Vector xdot, Vector odot) -> bool"""
        return _icub.ClientCartesianController_getTaskVelocities(self, xdot, odot)


    def setTaskVelocities(self, xdot, odot):
        """setTaskVelocities(ClientCartesianController self, Vector xdot, Vector odot) -> bool"""
        return _icub.ClientCartesianController_setTaskVelocities(self, xdot, odot)


    def attachTipFrame(self, x, o):
        """attachTipFrame(ClientCartesianController self, Vector x, Vector o) -> bool"""
        return _icub.ClientCartesianController_attachTipFrame(self, x, o)


    def getTipFrame(self, x, o):
        """getTipFrame(ClientCartesianController self, Vector x, Vector o) -> bool"""
        return _icub.ClientCartesianController_getTipFrame(self, x, o)


    def removeTipFrame(self):
        """removeTipFrame(ClientCartesianController self) -> bool"""
        return _icub.ClientCartesianController_removeTipFrame(self)


    def checkMotionDone(self, f):
        """checkMotionDone(ClientCartesianController self, bool * f) -> bool"""
        return _icub.ClientCartesianController_checkMotionDone(self, f)


    def waitMotionDone(self, period=0.1, timeout=0.0):
        """
        waitMotionDone(ClientCartesianController self, double const period=0.1, double const timeout=0.0) -> bool
        waitMotionDone(ClientCartesianController self, double const period=0.1) -> bool
        waitMotionDone(ClientCartesianController self) -> bool
        """
        return _icub.ClientCartesianController_waitMotionDone(self, period, timeout)


    def stopControl(self):
        """stopControl(ClientCartesianController self) -> bool"""
        return _icub.ClientCartesianController_stopControl(self)


    def storeContext(self, id):
        """storeContext(ClientCartesianController self, int * id) -> bool"""
        return _icub.ClientCartesianController_storeContext(self, id)


    def restoreContext(self, id):
        """restoreContext(ClientCartesianController self, int const id) -> bool"""
        return _icub.ClientCartesianController_restoreContext(self, id)


    def deleteContext(self, id):
        """deleteContext(ClientCartesianController self, int const id) -> bool"""
        return _icub.ClientCartesianController_deleteContext(self, id)


    def getInfo(self, info):
        """getInfo(ClientCartesianController self, Bottle info) -> bool"""
        return _icub.ClientCartesianController_getInfo(self, info)


    def registerEvent(self, event):
        """registerEvent(ClientCartesianController self, CartesianEvent event) -> bool"""
        return _icub.ClientCartesianController_registerEvent(self, event)


    def unregisterEvent(self, event):
        """unregisterEvent(ClientCartesianController self, CartesianEvent event) -> bool"""
        return _icub.ClientCartesianController_unregisterEvent(self, event)


    def tweakSet(self, options):
        """tweakSet(ClientCartesianController self, Bottle options) -> bool"""
        return _icub.ClientCartesianController_tweakSet(self, options)


    def tweakGet(self, options):
        """tweakGet(ClientCartesianController self, Bottle options) -> bool"""
        return _icub.ClientCartesianController_tweakGet(self, options)

    __swig_destroy__ = _icub.delete_ClientCartesianController
    __del__ = lambda self: None
ClientCartesianController_swigregister = _icub.ClientCartesianController_swigregister
ClientCartesianController_swigregister(ClientCartesianController)

class GazeEventHandler(yarp.BufferedPortBottle):
    """Proxy of C++ GazeEventHandler class."""

    __swig_setmethods__ = {}
    for _s in [yarp.BufferedPortBottle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GazeEventHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [yarp.BufferedPortBottle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GazeEventHandler, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def setInterface(self, interface):
        """setInterface(GazeEventHandler self, ClientGazeController interface)"""
        return _icub.GazeEventHandler_setInterface(self, interface)

    __swig_destroy__ = _icub.delete_GazeEventHandler
    __del__ = lambda self: None
GazeEventHandler_swigregister = _icub.GazeEventHandler_swigregister
GazeEventHandler_swigregister(GazeEventHandler)

class ClientGazeController(yarp.DeviceDriver, yarp.IGazeControl):
    """Proxy of C++ ClientGazeController class."""

    __swig_setmethods__ = {}
    for _s in [yarp.DeviceDriver, yarp.IGazeControl]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ClientGazeController, name, value)
    __swig_getmethods__ = {}
    for _s in [yarp.DeviceDriver, yarp.IGazeControl]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ClientGazeController, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(ClientGazeController self) -> ClientGazeController
        __init__(ClientGazeController self, Searchable config) -> ClientGazeController
        """
        this = _icub.new_ClientGazeController(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def open(self, config):
        """open(ClientGazeController self, Searchable config) -> bool"""
        return _icub.ClientGazeController_open(self, config)


    def close(self):
        """close(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_close(self)


    def setTrackingMode(self, f):
        """setTrackingMode(ClientGazeController self, bool const f) -> bool"""
        return _icub.ClientGazeController_setTrackingMode(self, f)


    def getTrackingMode(self, f):
        """getTrackingMode(ClientGazeController self, bool * f) -> bool"""
        return _icub.ClientGazeController_getTrackingMode(self, f)


    def setStabilizationMode(self, f):
        """setStabilizationMode(ClientGazeController self, bool const f) -> bool"""
        return _icub.ClientGazeController_setStabilizationMode(self, f)


    def getStabilizationMode(self, f):
        """getStabilizationMode(ClientGazeController self, bool * f) -> bool"""
        return _icub.ClientGazeController_getStabilizationMode(self, f)


    def getFixationPoint(self, fp, stamp=None):
        """
        getFixationPoint(ClientGazeController self, Vector fp, Stamp stamp=None) -> bool
        getFixationPoint(ClientGazeController self, Vector fp) -> bool
        """
        return _icub.ClientGazeController_getFixationPoint(self, fp, stamp)


    def getAngles(self, ang, stamp=None):
        """
        getAngles(ClientGazeController self, Vector ang, Stamp stamp=None) -> bool
        getAngles(ClientGazeController self, Vector ang) -> bool
        """
        return _icub.ClientGazeController_getAngles(self, ang, stamp)


    def lookAtFixationPoint(self, fp):
        """lookAtFixationPoint(ClientGazeController self, Vector fp) -> bool"""
        return _icub.ClientGazeController_lookAtFixationPoint(self, fp)


    def lookAtAbsAngles(self, ang):
        """lookAtAbsAngles(ClientGazeController self, Vector ang) -> bool"""
        return _icub.ClientGazeController_lookAtAbsAngles(self, ang)


    def lookAtRelAngles(self, ang):
        """lookAtRelAngles(ClientGazeController self, Vector ang) -> bool"""
        return _icub.ClientGazeController_lookAtRelAngles(self, ang)


    def lookAtMonoPixel(self, camSel, px, z=1.0):
        """
        lookAtMonoPixel(ClientGazeController self, int const camSel, Vector px, double const z=1.0) -> bool
        lookAtMonoPixel(ClientGazeController self, int const camSel, Vector px) -> bool
        """
        return _icub.ClientGazeController_lookAtMonoPixel(self, camSel, px, z)


    def lookAtMonoPixelWithVergence(self, camSel, px, ver):
        """lookAtMonoPixelWithVergence(ClientGazeController self, int const camSel, Vector px, double const ver) -> bool"""
        return _icub.ClientGazeController_lookAtMonoPixelWithVergence(self, camSel, px, ver)


    def lookAtStereoPixels(self, pxl, pxr):
        """lookAtStereoPixels(ClientGazeController self, Vector pxl, Vector pxr) -> bool"""
        return _icub.ClientGazeController_lookAtStereoPixels(self, pxl, pxr)


    def getNeckTrajTime(self, t):
        """getNeckTrajTime(ClientGazeController self, double * t) -> bool"""
        return _icub.ClientGazeController_getNeckTrajTime(self, t)


    def getEyesTrajTime(self, t):
        """getEyesTrajTime(ClientGazeController self, double * t) -> bool"""
        return _icub.ClientGazeController_getEyesTrajTime(self, t)


    def getVORGain(self, gain):
        """getVORGain(ClientGazeController self, double * gain) -> bool"""
        return _icub.ClientGazeController_getVORGain(self, gain)


    def getOCRGain(self, gain):
        """getOCRGain(ClientGazeController self, double * gain) -> bool"""
        return _icub.ClientGazeController_getOCRGain(self, gain)


    def getSaccadesMode(self, f):
        """getSaccadesMode(ClientGazeController self, bool * f) -> bool"""
        return _icub.ClientGazeController_getSaccadesMode(self, f)


    def getSaccadesInhibitionPeriod(self, period):
        """getSaccadesInhibitionPeriod(ClientGazeController self, double * period) -> bool"""
        return _icub.ClientGazeController_getSaccadesInhibitionPeriod(self, period)


    def getSaccadesActivationAngle(self, angle):
        """getSaccadesActivationAngle(ClientGazeController self, double * angle) -> bool"""
        return _icub.ClientGazeController_getSaccadesActivationAngle(self, angle)


    def getLeftEyePose(self, x, o, stamp=None):
        """
        getLeftEyePose(ClientGazeController self, Vector x, Vector o, Stamp stamp=None) -> bool
        getLeftEyePose(ClientGazeController self, Vector x, Vector o) -> bool
        """
        return _icub.ClientGazeController_getLeftEyePose(self, x, o, stamp)


    def getRightEyePose(self, x, o, stamp=None):
        """
        getRightEyePose(ClientGazeController self, Vector x, Vector o, Stamp stamp=None) -> bool
        getRightEyePose(ClientGazeController self, Vector x, Vector o) -> bool
        """
        return _icub.ClientGazeController_getRightEyePose(self, x, o, stamp)


    def getHeadPose(self, x, o, stamp=None):
        """
        getHeadPose(ClientGazeController self, Vector x, Vector o, Stamp stamp=None) -> bool
        getHeadPose(ClientGazeController self, Vector x, Vector o) -> bool
        """
        return _icub.ClientGazeController_getHeadPose(self, x, o, stamp)


    def get2DPixel(self, camSel, x, px):
        """get2DPixel(ClientGazeController self, int const camSel, Vector x, Vector px) -> bool"""
        return _icub.ClientGazeController_get2DPixel(self, camSel, x, px)


    def get3DPoint(self, camSel, px, z, x):
        """get3DPoint(ClientGazeController self, int const camSel, Vector px, double const z, Vector x) -> bool"""
        return _icub.ClientGazeController_get3DPoint(self, camSel, px, z, x)


    def get3DPointOnPlane(self, camSel, px, plane, x):
        """get3DPointOnPlane(ClientGazeController self, int const camSel, Vector px, Vector plane, Vector x) -> bool"""
        return _icub.ClientGazeController_get3DPointOnPlane(self, camSel, px, plane, x)


    def get3DPointFromAngles(self, mode, ang, x):
        """get3DPointFromAngles(ClientGazeController self, int const mode, Vector ang, Vector x) -> bool"""
        return _icub.ClientGazeController_get3DPointFromAngles(self, mode, ang, x)


    def getAnglesFrom3DPoint(self, x, ang):
        """getAnglesFrom3DPoint(ClientGazeController self, Vector x, Vector ang) -> bool"""
        return _icub.ClientGazeController_getAnglesFrom3DPoint(self, x, ang)


    def triangulate3DPoint(self, pxl, pxr, x):
        """triangulate3DPoint(ClientGazeController self, Vector pxl, Vector pxr, Vector x) -> bool"""
        return _icub.ClientGazeController_triangulate3DPoint(self, pxl, pxr, x)


    def getJointsDesired(self, qdes):
        """getJointsDesired(ClientGazeController self, Vector qdes) -> bool"""
        return _icub.ClientGazeController_getJointsDesired(self, qdes)


    def getJointsVelocities(self, qdot):
        """getJointsVelocities(ClientGazeController self, Vector qdot) -> bool"""
        return _icub.ClientGazeController_getJointsVelocities(self, qdot)


    def getStereoOptions(self, options):
        """getStereoOptions(ClientGazeController self, Bottle options) -> bool"""
        return _icub.ClientGazeController_getStereoOptions(self, options)


    def setNeckTrajTime(self, t):
        """setNeckTrajTime(ClientGazeController self, double const t) -> bool"""
        return _icub.ClientGazeController_setNeckTrajTime(self, t)


    def setEyesTrajTime(self, t):
        """setEyesTrajTime(ClientGazeController self, double const t) -> bool"""
        return _icub.ClientGazeController_setEyesTrajTime(self, t)


    def setVORGain(self, gain):
        """setVORGain(ClientGazeController self, double const gain) -> bool"""
        return _icub.ClientGazeController_setVORGain(self, gain)


    def setOCRGain(self, gain):
        """setOCRGain(ClientGazeController self, double const gain) -> bool"""
        return _icub.ClientGazeController_setOCRGain(self, gain)


    def setSaccadesMode(self, f):
        """setSaccadesMode(ClientGazeController self, bool const f) -> bool"""
        return _icub.ClientGazeController_setSaccadesMode(self, f)


    def setSaccadesInhibitionPeriod(self, period):
        """setSaccadesInhibitionPeriod(ClientGazeController self, double const period) -> bool"""
        return _icub.ClientGazeController_setSaccadesInhibitionPeriod(self, period)


    def setSaccadesActivationAngle(self, angle):
        """setSaccadesActivationAngle(ClientGazeController self, double const angle) -> bool"""
        return _icub.ClientGazeController_setSaccadesActivationAngle(self, angle)


    def setStereoOptions(self, options):
        """setStereoOptions(ClientGazeController self, Bottle options) -> bool"""
        return _icub.ClientGazeController_setStereoOptions(self, options)


    def bindNeckPitch(self, min, max):
        """bindNeckPitch(ClientGazeController self, double const min, double const max) -> bool"""
        return _icub.ClientGazeController_bindNeckPitch(self, min, max)


    def blockNeckPitch(self, *args):
        """
        blockNeckPitch(ClientGazeController self, double const val) -> bool
        blockNeckPitch(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_blockNeckPitch(self, *args)


    def bindNeckRoll(self, min, max):
        """bindNeckRoll(ClientGazeController self, double const min, double const max) -> bool"""
        return _icub.ClientGazeController_bindNeckRoll(self, min, max)


    def blockNeckRoll(self, *args):
        """
        blockNeckRoll(ClientGazeController self, double const val) -> bool
        blockNeckRoll(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_blockNeckRoll(self, *args)


    def bindNeckYaw(self, min, max):
        """bindNeckYaw(ClientGazeController self, double const min, double const max) -> bool"""
        return _icub.ClientGazeController_bindNeckYaw(self, min, max)


    def blockNeckYaw(self, *args):
        """
        blockNeckYaw(ClientGazeController self, double const val) -> bool
        blockNeckYaw(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_blockNeckYaw(self, *args)


    def blockEyes(self, *args):
        """
        blockEyes(ClientGazeController self, double const ver) -> bool
        blockEyes(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_blockEyes(self, *args)


    def getNeckPitchRange(self, min, max):
        """getNeckPitchRange(ClientGazeController self, double * min, double * max) -> bool"""
        return _icub.ClientGazeController_getNeckPitchRange(self, min, max)


    def getNeckRollRange(self, min, max):
        """getNeckRollRange(ClientGazeController self, double * min, double * max) -> bool"""
        return _icub.ClientGazeController_getNeckRollRange(self, min, max)


    def getNeckYawRange(self, min, max):
        """getNeckYawRange(ClientGazeController self, double * min, double * max) -> bool"""
        return _icub.ClientGazeController_getNeckYawRange(self, min, max)


    def getBlockedVergence(self, ver):
        """getBlockedVergence(ClientGazeController self, double * ver) -> bool"""
        return _icub.ClientGazeController_getBlockedVergence(self, ver)


    def clearNeckPitch(self):
        """clearNeckPitch(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_clearNeckPitch(self)


    def clearNeckRoll(self):
        """clearNeckRoll(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_clearNeckRoll(self)


    def clearNeckYaw(self):
        """clearNeckYaw(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_clearNeckYaw(self)


    def clearEyes(self):
        """clearEyes(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_clearEyes(self)


    def getNeckAngleUserTolerance(self, angle):
        """getNeckAngleUserTolerance(ClientGazeController self, double * angle) -> bool"""
        return _icub.ClientGazeController_getNeckAngleUserTolerance(self, angle)


    def setNeckAngleUserTolerance(self, angle):
        """setNeckAngleUserTolerance(ClientGazeController self, double const angle) -> bool"""
        return _icub.ClientGazeController_setNeckAngleUserTolerance(self, angle)


    def checkMotionDone(self, f):
        """checkMotionDone(ClientGazeController self, bool * f) -> bool"""
        return _icub.ClientGazeController_checkMotionDone(self, f)


    def waitMotionDone(self, period=0.1, timeout=0.0):
        """
        waitMotionDone(ClientGazeController self, double const period=0.1, double const timeout=0.0) -> bool
        waitMotionDone(ClientGazeController self, double const period=0.1) -> bool
        waitMotionDone(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_waitMotionDone(self, period, timeout)


    def checkSaccadeDone(self, f):
        """checkSaccadeDone(ClientGazeController self, bool * f) -> bool"""
        return _icub.ClientGazeController_checkSaccadeDone(self, f)


    def waitSaccadeDone(self, period=0.1, timeout=0.0):
        """
        waitSaccadeDone(ClientGazeController self, double const period=0.1, double const timeout=0.0) -> bool
        waitSaccadeDone(ClientGazeController self, double const period=0.1) -> bool
        waitSaccadeDone(ClientGazeController self) -> bool
        """
        return _icub.ClientGazeController_waitSaccadeDone(self, period, timeout)


    def stopControl(self):
        """stopControl(ClientGazeController self) -> bool"""
        return _icub.ClientGazeController_stopControl(self)


    def storeContext(self, id):
        """storeContext(ClientGazeController self, int * id) -> bool"""
        return _icub.ClientGazeController_storeContext(self, id)


    def restoreContext(self, id):
        """restoreContext(ClientGazeController self, int const id) -> bool"""
        return _icub.ClientGazeController_restoreContext(self, id)


    def deleteContext(self, id):
        """deleteContext(ClientGazeController self, int const id) -> bool"""
        return _icub.ClientGazeController_deleteContext(self, id)


    def getInfo(self, info):
        """getInfo(ClientGazeController self, Bottle info) -> bool"""
        return _icub.ClientGazeController_getInfo(self, info)


    def registerEvent(self, event):
        """registerEvent(ClientGazeController self, GazeEvent event) -> bool"""
        return _icub.ClientGazeController_registerEvent(self, event)


    def unregisterEvent(self, event):
        """unregisterEvent(ClientGazeController self, GazeEvent event) -> bool"""
        return _icub.ClientGazeController_unregisterEvent(self, event)


    def tweakSet(self, options):
        """tweakSet(ClientGazeController self, Bottle options) -> bool"""
        return _icub.ClientGazeController_tweakSet(self, options)


    def tweakGet(self, options):
        """tweakGet(ClientGazeController self, Bottle options) -> bool"""
        return _icub.ClientGazeController_tweakGet(self, options)

    __swig_destroy__ = _icub.delete_ClientGazeController
    __del__ = lambda self: None
ClientGazeController_swigregister = _icub.ClientGazeController_swigregister
ClientGazeController_swigregister(ClientGazeController)


def init():
    """init() -> bool"""
    return _icub.init()
# This file is compatible with both classic and new-style classes.


