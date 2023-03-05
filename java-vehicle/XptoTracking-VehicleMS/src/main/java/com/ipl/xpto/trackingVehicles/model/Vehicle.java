package com.ipl.xpto.trackingVehicles.model;

import java.util.UUID;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "vehicles")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Vehicle implements IEntity<UUID>{

	@Id
	@Column(name = "vehicleId")
	@GeneratedValue(strategy = GenerationType.AUTO)
	private UUID id;

	@Column(name = "customerOwner")
	private UUID customerOwner;
	
	@Column(name = "telemetryProfile")
	private UUID telemetryProfile;
	
	@Column(name = "currentDriver")
	private UUID currentDriver;
	
	@Column(name = "numberPlate")
	private String numberPlate;
	
	@Column(name = "vin")
	private String vin;
	
	@Column(name = "color")
	private String color;

	public UUID getId() {
		return id;
	}

	public String getVin() {
		return vin;
	}

	public void setVin(String vin) {
		this.vin = vin;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getColor() {
		return color;
	}

	public void setNumberPlate(String numberPlate) {
		this.numberPlate = numberPlate.toLowerCase();
	}

	public String getNumberPlate() {
		return numberPlate;
	}

	public void setTelemetryProfile(UUID telemetryProfile) {
		this.telemetryProfile = telemetryProfile;
	}

	public UUID getTelemetryProfile() {
		return telemetryProfile;
	}

	public void setCustomerOwner(UUID customerOwner) {
		this.customerOwner = customerOwner;
	}

	public UUID getCustomerOwner() {
		return customerOwner;
	}

	public void setCurrentDriver(UUID currentDriver) {
		this.currentDriver = currentDriver;
	}

	public UUID getCurrentDriver() {
		return currentDriver;
	}

}
