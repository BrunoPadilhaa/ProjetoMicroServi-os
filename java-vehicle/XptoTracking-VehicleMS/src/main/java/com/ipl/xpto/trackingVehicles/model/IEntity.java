package com.ipl.xpto.trackingVehicles.model;

import java.io.Serializable;

public interface IEntity<T extends Serializable> {
  
  public T getId();

}
