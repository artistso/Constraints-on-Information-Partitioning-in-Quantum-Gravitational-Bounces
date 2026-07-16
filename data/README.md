# Data and Phenomenology Policy

This directory remains documentation-only until a model passes the phenomenology feasibility gate.

## Required provenance for any dataset

- Dataset or archive name.
- Producing instrument or collaboration.
- Version and access date.
- Persistent identifier or official source.
- License and redistribution conditions.
- Selection cuts applied locally.
- Checksums for immutable local inputs when permitted.
- Script that transforms the source data into analysis-ready products.

## No raw-data commitment yet

The project has not selected a validated observational signal. Accordingly, it does not yet claim that Rubin, gamma-ray, radio, ultraviolet, astrometric, or gravitational-wave data provide a viable search channel.

## Phenomenology gate

Data acquisition begins only when the selected model supplies:

1. event-rate law;
2. emitted energy and spectrum;
3. intrinsic duration and light curve;
4. population and distance distribution;
5. propagation and attenuation model;
6. instrument response overlap;
7. background population;
8. statistical upper-limit or detection plan.

## Directory convention after gate approval

```text
data/
  external/      # immutable references or download manifests
  interim/       # transformed intermediate products
  processed/     # analysis-ready derived data
  simulations/   # injected signals and background simulations
  provenance/    # licenses, checksums, versions, and metadata
```

Large files should not be committed directly to Git. Use release assets, an archival repository, or a documented external store with checksums.
