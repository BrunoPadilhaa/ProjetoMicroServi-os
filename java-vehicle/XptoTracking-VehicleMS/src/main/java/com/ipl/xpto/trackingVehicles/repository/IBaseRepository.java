package com.ipl.xpto.trackingVehicles.repository;

import com.ipl.xpto.trackingVehicles.model.IEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;

import java.io.Serializable;

@NoRepositoryBean
public interface IBaseRepository<ENTITY extends IEntity<?>, ID extends Serializable> extends JpaRepository<ENTITY, ID>   {

}
