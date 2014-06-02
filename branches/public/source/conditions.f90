!*******************************************************************************
! Conditions.f90 3/26/12
! This file contains modules associated with the thermodynamic conditions in 
! the matter undergoing nucleosynthesis  
!*******************************************************************************
  
Module conditions
!===============================================================================
! This module contains data on the current time and thermodynamic conditions.
!===============================================================================
  Real(8) :: t         ! Time at the beginning of the current timestep
  Real(8) :: tt        ! Trial time for End of current timestep
  Real(8) :: to        ! Time at the beginning of the previous timestep
  Real(8) :: tdel      ! Trial duration of timestep
  Real(8) :: tdel_next ! Integrator estimate of duration for next timestep
  Real(8) :: t9t,rhot  ! Temperature (GK) and Density (g/cc) at trial time
  
! Threading Scope
!$OMP THREADPRIVATE(t,tt,tdel,tdel_next,t9t,rhot)
  
End Module conditions
  
Module thermo_data
!===============================================================================
! This module contains the thermodynamic trajectory which the network follows
!===============================================================================
  Integer, Parameter   :: nhmx=50000 ! The max number of thermo points
  Integer              :: nh        ! The actual number of points
  Real(8) :: tstart,tstop,th(nhmx),t9h(nhmx),rhoh(nhmx)
! Real(8) :: yeh(nhmx)       !NSE
  
! Threading Scope
!$OMP THREADPRIVATE(nh,tstart,tstop,th,t9h,rhoh)
!!$OMP THREADPRIVATE(yeh)     !NSE
  
End Module thermo_data
  
