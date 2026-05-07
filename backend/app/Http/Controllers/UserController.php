<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;

class UserController extends Controller
{
    public function register(Request $request)
    {
        $request->validate([
            'nome' => 'required',
            'email' => 'required|email|unique:users,email',
            'senha' => 'required|min:6',
            'tipo' => 'required'
        ]);

        $user = User::create([
            'nome' => $request->nome,
            'email' => $request->email,
            'senha' => bcrypt($request->senha),
            'tipo' => $request->tipo
        ]);

        return response()->json($user, 201);
    }

    public function index()
    {
        return User::all();
    }
}
