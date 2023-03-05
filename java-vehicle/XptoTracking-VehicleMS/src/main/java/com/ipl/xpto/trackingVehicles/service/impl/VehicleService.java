package com.ipl.xpto.trackingVehicles.service.impl;

import com.ipl.xpto.trackingVehicles.model.Vehicle;
import com.ipl.xpto.trackingVehicles.repository.VehicleRepository;
import com.ipl.xpto.trackingVehicles.service.IVehicleService;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class VehicleService extends BaseEntityService<UUID, Vehicle, VehicleRepository> implements IVehicleService {

	public VehicleService(VehicleRepository repository) {
		super(repository);
	}


}
