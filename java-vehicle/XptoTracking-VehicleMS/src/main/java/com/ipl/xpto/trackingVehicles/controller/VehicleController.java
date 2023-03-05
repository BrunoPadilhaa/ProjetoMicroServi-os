package com.ipl.xpto.trackingVehicles.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ipl.xpto.trackingVehicles.model.Vehicle;
import com.ipl.xpto.trackingVehicles.repository.VehicleRepository;


@RestController
@RequiredArgsConstructor
@RequestMapping("/tracking")
public class VehicleController {

  @Autowired
  VehicleRepository vehicleRepo;

  @GetMapping("/vehicles")
  public ResponseEntity<List<Vehicle>> listVehicles() {
    try {
      List<Vehicle> vehicles = new ArrayList<Vehicle>();

      vehicleRepo.findAll().forEach(vehicles::add);

      if (vehicles.isEmpty()) {
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
      }

      return new ResponseEntity<>(vehicles, HttpStatus.OK);
    } catch (Exception e) {
      return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

    @GetMapping("/vehicles/plate/{plate}")
    public ResponseEntity<List<Vehicle>> listVehiclesByPlate(@PathVariable("plate") String plate) {
        try {
            List<Vehicle> vehicles = new ArrayList<Vehicle>();

            vehicleRepo.findByNumberPlate(plate.toLowerCase()).forEach(vehicles::add);

            if (vehicles.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(vehicles, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

  @GetMapping("/vehicles/{id}")
  public ResponseEntity<Vehicle> getVehicle(@PathVariable("id") UUID id) {
    Optional<Vehicle> vehicleData = vehicleRepo.findById(id);

    if (vehicleData.isPresent()) {
      return new ResponseEntity<>(vehicleData.get(), HttpStatus.OK);
    } else {
      return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
  }

  @PostMapping("/vehicles")
  public ResponseEntity<Vehicle> createVehicle(@RequestBody Vehicle vehicle) {
    try {
    	Vehicle _vehicle = vehicleRepo.save(
    			new Vehicle(
                        null,
                        vehicle.getCustomerOwner(),
    					vehicle.getTelemetryProfile(),
                        vehicle.getCurrentDriver(),
                        vehicle.getNumberPlate(),
    					vehicle.getVin(),
                        vehicle.getColor()));
      return new ResponseEntity<>(_vehicle, HttpStatus.CREATED);
    } catch (Exception e) {
      return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

  @PutMapping("/vehicles/{id}")
  public ResponseEntity<Vehicle> updateVehicle(@PathVariable("id") UUID id, @RequestBody Vehicle vehicle) {
    Optional<Vehicle> vehicleData = vehicleRepo.findById(id);

    if (vehicleData.isPresent()) {
		Vehicle _vehicle = vehicleData.get();
		
		_vehicle.setColor(vehicle.getColor());
		_vehicle.setVin(vehicle.getVin());
		_vehicle.setNumberPlate(vehicle.getNumberPlate());
		_vehicle.setTelemetryProfile(vehicle.getTelemetryProfile());
		_vehicle.setCustomerOwner(vehicle.getCustomerOwner());
		_vehicle.setCurrentDriver(vehicle.getCurrentDriver());
		
      return new ResponseEntity<>(vehicleRepo.save(_vehicle), HttpStatus.OK);
    } else {
      return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
  }

  @DeleteMapping("/vehicles/{id}")
  public ResponseEntity<HttpStatus> deleteVehicle(@PathVariable("id") UUID id) {
    try {
    	vehicleRepo.deleteById(id);
      return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    } catch (Exception e) {
      return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }


}