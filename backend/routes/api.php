<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\VehicleController;
use App\Http\Controllers\UserController;

Route::post('/register', [UserController::class, 'register']);
Route::get('/users', [UserController::class, 'index']);

Route::get('/teste', function () {
    return "API funcionando!";
});

Route::get('/vehicles', [VehicleController::class, 'index']);
Route::post('/vehicles', [VehicleController::class, 'store']);

Route::put('/vehicle-exit/{placa}', [VehicleController::class, 'exit']);
