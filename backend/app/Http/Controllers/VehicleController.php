<?php

/*
|--------------------------------------------------------------------------
| SmartPark
| Autor: Cristiano Junior
| TCC 2026
|--------------------------------------------------------------------------
*/

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Vehicle;

class VehicleController extends Controller
{
    public function index()
    {
        return Vehicle::all();
    }

    public function store(Request $request)
    {
        $vehicle = Vehicle::create([
            'placa' => $request->placa,
            'modelo' => $request->modelo,
            'cor' => $request->cor,
            'fabricante' => $request->fabricante,
            'status' => 'estacionado'
        ]);

        return response()->json($vehicle, 201);
    }

    public function exit($placa)
    {
        $vehicle = Vehicle::where('placa', $placa)->first();

        if (!$vehicle) {
            return response()->json([
                'message' => 'Veículo não encontrado'
            ], 404);
        }

        $vehicle->status = 'saiu';
        $vehicle->save();

        return response()->json([
            'message' => 'Saída registrada com sucesso',
            'vehicle' => $vehicle
        ]);
    }
}
