import { useContext } from "react";
import { AuthContext } from "../context/JWTContext";

export const useAuth = () => useContext(AuthContext);
